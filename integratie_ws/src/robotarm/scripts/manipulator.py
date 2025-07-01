#!/usr/bin/env python
'''
Type: python script
Naam programma: manipulator

Programmeur: Ruben van Halteren
Studentnummer: 2214688

Vak: Robotica in de machinebouw
Locatie: Breda
Datum: 12-6-2025
Versie: 1.2

Functionele beschrijving:
Oppakken van tandenborstel, waarvan de positie en het type is doorgestuurd vanuit het vision systeem via topic pose_tb_camera en type_tb.
Vervolgens wordt de tandenborstel gesorteerd in 1 van de 4 sorteerbakken, afhankelijk van het type tandenborstel.

Deelfuncties:
1. Initialiseren van Node: manipulator_node
2. Activatie van bewegingen manipulator bij het sturen van een goal naar manipulator_action.
3. Pose tandenborstel t.o.v. camera link terugtransformeren naar planning frame 'world'.
4. Bewegen naar tandenborstel en gripper sluiten.
5. Tandenborstel mesh toevoegen aan planning scene.
6. Bewegen naar sorteerbak en gripper openen.
7. Tandenborstel verwijderen uit planning scene.
8. Bewegen naar veiligheidspunt boven transportband.
'''

import rospy
import sys
import moveit_commander
from std_msgs.msg import Int32   
from xarm_msgs.srv import SetInt16, Call
import actionlib
from robotarm.msg import manipulatorAction, manipulatorFeedback, manipulatorResult
import tf2_ros
from geometry_msgs.msg import PoseStamped, Pose, Point, Quaternion
from tf2_geometry_msgs.tf2_geometry_msgs import do_transform_pose
import moveit_msgs.msg
import time
import copy
import rospkg

class unit_manipulator:
    def __init__(self):
        #positie object t.o.v. camera assenstelsel
        self.positie_object_vanuit_camera = None
        #getransformeerde coordinaten
        self.positie_object_vanuit_base = None
        #positie waar gripper gesloten kan worden
        self.positie_object_oppakken = None
        #een getal dat aanduid welk type tandenborstel is gedecteerd
        self.type_tandenborstel = None
        #getal waarmee gripper kan worden gesloten
        self.GRIPPER_DICHT = 0
        #getal waarmee gripper kan worden geopend
        self.GRIPPER_OPEN = 1

        self.vaste_posities = {
            # bak0 / blauw
            0: ((-0.2100 , 0.35 , 0.17), (-0.6755 ,-0.7364 ,-0.0366 , 0.0057)), 
            
            # bak1 / kopstuk
            4: ((-0.1103 , 0.35 , 0.17), (-0.7318 ,-0.6803 ,-0.0346 , 0.0224)),
            
            # bak2 / paars
            3: ((-0.2108 , 0.24 , 0.0501), (0.7099 ,-0.7042 ,0.0060 , 0.0002)),
            
            # bak3 / geel
            2: ((-0.1119 , 0.26 , 0.0565), (-0.6901 ,0.7236 ,0.0058 , 0.0090)),
            
            # russtand boven transportband
            10: ((-0.0345 , -0.2287 , 0.1078), (0.9436 ,-0.2732 ,0.1624 , 0.0926)),
        }

        # positie tandenborstel mesh t.o.v. van uiteinde gripper
        self.tandenborstel_pose = PoseStamped()
        self.tandenborstel_pose.header.frame_id = "link_tcp"
        self.tandenborstel_pose.pose.orientation.x = 0 
        self.tandenborstel_pose.pose.orientation.y = 0
        self.tandenborstel_pose.pose.orientation.z = 0.9
        self.tandenborstel_pose.pose.orientation.w = 1.0  
        self.tandenborstel_pose.pose.position.x = 0.0
        self.tandenborstel_pose.pose.position.y = 0.0
        self.tandenborstel_pose.pose.position.z = -0.02

        #moveIt instellingen
        moveit_commander.roscpp_initialize(sys.argv)
        self.robot = moveit_commander.RobotCommander()
        self.scene = moveit_commander.PlanningSceneInterface()
        self.group = moveit_commander.MoveGroupCommander('arm')
        self.group.set_max_velocity_scaling_factor(0.2)      
        self.group.set_max_acceleration_scaling_factor(0.05)
        self.group.set_num_planning_attempts(50)
        self.group.set_planning_time(15)

        #Bewegingen in Rviz publiseren
        self.display_trajectory_publisher = rospy.Publisher(
            '/move_group/display_planned_path',
            moveit_msgs.msg.DisplayTrajectory,
            queue_size=20)

        #opslag voor transformeer data
        self.tf_buffer = tf2_ros.Buffer()
        # om benodigde transformatie en rotatie op te halen voor het terugtransformeren
        tf2_ros.TransformListener(self.tf_buffer)

        #subscribers voor topics uit vision-systeem
        rospy.Subscriber('/pos_tb_camera', PoseStamped, self.positie_callback)
        rospy.Subscriber('/type_tb', Int32, self.type_callback)

        #declaren variabelen voor feedback sturen en result
        self.feedback = manipulatorFeedback()
        self.result = manipulatorResult()
        
        # Action server aanmaken en starten
        self.action_server = actionlib.SimpleActionServer('manipulator_action', manipulatorAction, self.start_manipulator, True)
        rospy.loginfo("Manipulator action server gestart")

    def start_manipulator(self, goal): 
        if not self.gripper_openen():
            self.foutafhandeling()
            return

        if not self.transformeren():
           self.foutafhandeling()
           return 

        if not self.naar_tandenborstel():
            self.foutafhandeling()
            return 

        if not self.gripper_sluiten():
            self.foutafhandeling()
            return

        self.feedback.tandenborstel_opgepakt = True
        self.action_server.publish_feedback(self.feedback)

        if not self.spawn_tandenborstel():
            self.foutafhandeling()
            return

        if not self.naar_vaste_positie(self.type_tandenborstel):
            self.foutafhandeling()
            return  

        if not self.gripper_openen():
            self.foutafhandeling()
            return

        self.result.tandenborstel_gesorteerd = True
        self.action_server.set_succeeded(self.result)
        
        if not self.verwijder_tandenborstel():
            self.foutafhandeling()
            return

        rospy.sleep(1)
        
        if not self.gripper_uitschakelen():
            self.foutafhandeling()
            return
        

        if not self.naar_vaste_positie(10):
            self.foutafhandeling()
            return 

    def positie_callback(self, msg):
        self.positie_object_vanuit_camera = msg
            
    
    def type_callback(self, msg):
        self.type_tandenborstel = msg.data

    def transformeren(self):
        try:
            if self.positie_object_vanuit_camera is None or self.type_tandenborstel is None:
                rospy.logerr("Ontbrekende gegevens: positie of type tandenborstel is nog niet ontvangen van visionsysteem.")
                return False

            transform = self.tf_buffer.lookup_transform('world', self.positie_object_vanuit_camera.header.frame_id, 
            rospy.Time(0), rospy.Duration(1.0))
            getransformeerde_posestamped = do_transform_pose(self.positie_object_vanuit_camera, transform)
            rospy.loginfo("Coordinaten tandenborstel terug getransformeerd")
            self.positie_object_vanuit_base = getransformeerde_posestamped.pose
            return True

        except (tf2_ros.LookupException, tf2_ros.ConnectivityException, tf2_ros.ExtrapolationException) as e:
            rospy.logerr("error bij transformeren: "+ str(e))
            return False
        
            

    def naar_tandenborstel(self):
        try:
            success = self.plan_en_executeer(self.positie_object_vanuit_base)
            if not success:
                rospy.logerr("Beweging naar positie boven tandenborstel mislukt")
                return False
            
            rospy.loginfo("Beweging naar positie boven tandenborstel gelukt")

            self.positie_object_oppakken = copy.deepcopy(self.positie_object_vanuit_base)

            #gripper bevind zich rechtboven tandenborstel en moet alleen dalen tot een bepaalde hoogte.
            self.positie_object_oppakken.position.z = 0.0495
            
            success = self.plan_en_executeer(self.positie_object_oppakken)
            if not success:
                rospy.logerr("Beweging naar positie op hoogte tandenborstel mislukt")
                return False
            
            rospy.loginfo("Beweging tot hoogte tandenborstel gelukt")

            return True

        except Exception as e:
            rospy.logerr("exception error bij het bewegen richting de tandenborstel: "+ str(e))  
            return False

    def naar_vaste_positie(self, locatie):
        try: 
            positie, orientatie = self.vaste_posities[locatie]
            pose_target = Pose()
            pose_target.position.x = positie[0]
            pose_target.position.y = positie[1]
            pose_target.position.z = positie[2]
            pose_target.orientation.x = orientatie[0]
            pose_target.orientation.y = orientatie[1]
            pose_target.orientation.z = orientatie[2]
            pose_target.orientation.w = orientatie[3]

            success = self.plan_en_executeer(pose_target)

            if not success:
                rospy.logerr("Bewegen naar vaste positie " + str(locatie) +" mislukt")
                return False
            
            rospy.loginfo("Bewegen naar vaste positie " + str(locatie) +  " gelukt")
            
            
            return True
    
        except Exception as e:
            rospy.logerr("exception error bij het bewegen richting vaste positie "+ str(locatie) + " " + str(e))    
            return False  


    def plan_en_executeer(self, pose_target):
        try:
            self.group.set_start_state_to_current_state()
            self.group.set_pose_target(pose_target)
            plan = self.group.plan() # laat ook in Rviz zien hoe die plant

            if not plan or not plan.joint_trajectory.points:
                rospy.logerr("Plannen mislukt: geen trajectory gegenereerd")
                return False

            success = self.group.execute(plan, wait=True)
            self.group.clear_pose_targets()

            if not success:
                rospy.logerr("Uitvoeren van plan mislukt")
                return False

            return True

        except Exception as e: 
            rospy.logerr("exception error bij het plannen en bewegen: ")
            return False  

    def gripper_openen(self):
        try:
            rospy.wait_for_service('/ufactory/vacuum_gripper_set')
            gripper = rospy.ServiceProxy('/ufactory/vacuum_gripper_set', SetInt16)
            toegestane_timeout =rospy.Duration(5)  # seconden
            start = rospy.Time.now()
            while True:
                resp = gripper(self.GRIPPER_OPEN)
                if resp.ret ==0:
                    rospy.loginfo("gripper geopend")
                    return True
                if rospy.Time.now() - start > toegestane_timeout:
                    rospy.logerr("Fout: Gripper opent niet!")
                    return False
                time.sleep(0.1)
        except Exception as e:
            rospy.logerr("exception error bij het openen van gripper: "+ str(e))  
            return False

    def gripper_sluiten(self):
        try:
            rospy.wait_for_service('/ufactory/vacuum_gripper_set')
            gripper = rospy.ServiceProxy('/ufactory/vacuum_gripper_set', SetInt16)
            resp = gripper(self.GRIPPER_DICHT)
            return True
        except Exception as e:
            rospy.logerr("exception error bij het sluiten van gripper: "+ str(e))  
            return False
            
    def gripper_uitschakelen(self):
        try: 
            rospy.wait_for_service('/ufactory/stop_lite6_gripper')
            gripper = rospy.ServiceProxy('/ufactory/stop_lite6_gripper', Call)
            resp = gripper()
            return True
        except rospy.ServiceException as e:
            rospy.logerr("Uitschakelen van gripper faalde: "+ str(e))
            return False

    def spawn_tandenborstel(self):
        try: 
            rospack = rospkg.RosPack()
            package_path = rospack.get_path('robotarm')
            mesh_path = package_path + '/mesh/tandenborstel.stl'
            self.scene.add_mesh("tandenborstel", self.tandenborstel_pose, mesh_path, size=(1, 1, 1))
            rospy.sleep(0.1)
            touch_links = self.robot.get_link_names(group="arm")
            self.scene.attach_mesh("link_tcp", "tandenborstel", touch_links=touch_links)
            rospy.sleep(0.1)
            return True
        except rospy.ServiceException as e:
            rospy.logwarn("spawnen van tandenborstel faalde: "+ str(e))
            return False


    def verwijder_tandenborstel(self):
        try: 
            self.scene.remove_attached_object("link_tcp", name="tandenborstel")
            rospy.sleep(0.1)
            self.scene.remove_world_object("tandenborstel")
            rospy.sleep(0.1)
            return True
        
        except rospy.ServiceException as e:
            rospy.logwarn("verwijderen van tandenborstel faalde: "+ str(e))
            return False



    def foutafhandeling(self):
        self.result.tandenborstel_gesorteerd = False
        self.action_server.set_aborted(self.result)
        #controleer of tandenborstel is toegevoegd aan de wereld
        known = "tandenborstel" in self.scene.get_known_object_names()
        if known:
            self.verwijder_tandenborstel()
        self.gripper_uitschakelen()

if __name__ == "__main__":
    rospy.init_node('manipulator_node')
    manipulator = unit_manipulator()
    rospy.spin()