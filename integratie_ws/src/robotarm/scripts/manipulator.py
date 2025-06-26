#!/usr/bin/env python
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
            0: ((-0.2100 , 0.3000 , 0.1725), (-0.6755 ,-0.7364 ,-0.0366 , 0.0057)), 
            # bak1 / kopstuk
            4: ((-0.1103 , 0.3000 , 0.1725), (-0.7318 ,-0.6803 ,-0.0346 , 0.0224)),
            # bak2 / paars
            3: ((-0.2190 , 0.2291 , 0.0565), (-0.6281 ,0.7781 ,0.0053 , 0.0034)),
            # bak3/ geel
            2: ((-0.1183 , 0.2291 , 0.0565), (-0.6281 ,0.7781 ,0.0053 , 0.0034)),
            #russtand boven transportband
            10: ((-0.0345 , -0.2287 , 0.1078), (0.9436 ,-0.2732 ,0.1624 , 0.0926)),
        }

        moveit_commander.roscpp_initialize(sys.argv)
        self.robot = moveit_commander.RobotCommander()
        self.scene = moveit_commander.PlanningSceneInterface()
        self.group = moveit_commander.MoveGroupCommander('arm')
        self.group.set_max_velocity_scaling_factor(0.2)      
        self.group.set_max_acceleration_scaling_factor(0.05)
        self.group.set_num_planning_attempts(5)
        self.group.set_planning_time(10)

        self.display_trajectory_publisher = rospy.Publisher(
            '/move_group/display_planned_path',
            moveit_msgs.msg.DisplayTrajectory,
            queue_size=20)

        self.tf_buffer = tf2_ros.Buffer()
        tf2_ros.TransformListener(self.tf_buffer)

        rospy.Subscriber('/pos_tb_camera', PoseStamped, self.positie_callback)
        rospy.Subscriber('/type_tb', Int32, self.type_callback)

        self.feedback = manipulatorFeedback()
        self.result = manipulatorResult()
        
        # Action server aanmaken en starten
        self.action_server = actionlib.SimpleActionServer('manipulator_action', manipulatorAction, self.start_manipulator, False)
        self.action_server.start()
        rospy.loginfo("Manipulator action server gestart")

    def start_manipulator(self, goal):   
        # self.gripper_openen() 


        if not self.transformeren():
           self.foutafhandeling()
           return 
         

        if not self.naar_tandenborstel():
           self.foutafhandeling()
           return 

        # self.gripper_sluiten()

        self.feedback.tandenborstel_opgepakt = True
        self.action_server.publish_feedback(self.feedback)

        self.voeg_tandenborstel_toe_als_collision_mesh()

        if not self.naar_vaste_positie(self.type_tandenborstel):
            self.foutafhandeling()
            return  

        # self.gripper_openen()

        self.result.tandenborstel_gesorteerd = True
        self.action_server.set_succeeded(self.result)
        self.verwijder_tandenborstel_mesh()

        rospy.sleep(1)
        # Gripper uitzetten aan het einde
        # if not self.gripper_uitschakelen():
        #     self.foutafhandeling()
        #     return

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
                self.foutafhandeling()
                return False

            transform = self.tf_buffer.lookup_transform('world', self.positie_object_vanuit_camera.header.frame_id, 
            rospy.Time(0), rospy.Duration(1.0))
            self.positie_object_vanuit_base = do_transform_pose(self.positie_object_vanuit_camera, transform)
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

            self.positie_object_oppakken = copy.deepcopy(self.positie_object_vanuit_base.pose)

            #gripper bevind zich rechtboven tandenborstel en moet alleen dalen tot een bepaalde hoogte.
            self.positie_object_oppakken.position.z = 0.0501
            
            success = self.plan_en_executeer(self.positie_object_oppakken)
            if not success:
                rospy.logerr("Beweging naar positie op hoogte tandenborstel mislukt")
                return False

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
                pose_target.position.z -= 0.02

                success = self.plan_en_executeer(pose_target)
            
                if not success:
                    rospy.logerr("Bewegen naar binnekant bakje " + str(locatie) +" mislukt")
                    return False
            
            return True
    
        except Exception as e:
            rospy.logerr("exception error bij het bewegen richting vaste positie"+ str(locatie) + str(e))    
            return False  


    def plan_en_executeer(self, pose_target):
        try:
            self.group.set_start_state_to_current_state()
            self.group.set_pose_target(pose_target)
            plan = self.group.plan()

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
            return False  

    def gripper_openen(self):
        rospy.wait_for_service('/ufactory/vacuum_gripper_set')
        gripper = rospy.ServiceProxy('/ufactory/vacuum_gripper_set', SetInt16)

        toegestane_timeout =rospy.Duration(5)  # seconden
        start = rospy.Time.now()
        while True:
            resp = gripper(self.GRIPPER_OPEN)
            if resp.ret ==0:
                 return
            if rospy.Time.now() - start > toegestane_timeout:
                 rospy.logerr("Fout: Gripper opent niet!")
                 return
            time.sleep(0.1)

    
    def gripper_sluiten(self):
        rospy.wait_for_service('/ufactory/vacuum_gripper_set')
        gripper = rospy.ServiceProxy('/ufactory/vacuum_gripper_set', SetInt16)
        resp = gripper(self.GRIPPER_DICHT)
            


    def gripper_uitschakelen(self):
        try: 
            rospy.wait_for_service('/ufactory/stop_lite6_gripper')
            gripper = rospy.ServiceProxy('/ufactory/stop_lite6_gripper', Call)
            resp = gripper()
            return True
        except rospy.ServiceException as e:
            rospy.logwarn("Uitschakelen van gripper faalde: "+ str(e))
            return False

    def voeg_tandenborstel_toe_als_collision_mesh(self):
        tandenborstel_pose = PoseStamped()
        tandenborstel_pose.header.frame_id = "link_tcp"
        tandenborstel_pose.pose.orientation.x = 0 
        tandenborstel_pose.pose.orientation.y = 0
        tandenborstel_pose.pose.orientation.z = 0.9
        tandenborstel_pose.pose.orientation.w = 1.0  
        tandenborstel_pose.pose.position.x = 0.0
        tandenborstel_pose.pose.position.y = 0.0
        tandenborstel_pose.pose.position.z = -0.02

        rospack = rospkg.RosPack()
        package_path = rospack.get_path('robotarm')
        mesh_path = package_path + '/mesh/tandenborstel.stl'

        self.scene.add_mesh("tandenborstel", tandenborstel_pose, mesh_path, size=(1, 1, 1))
        rospy.sleep(1)

        touch_links = self.robot.get_link_names(group="arm")
        self.scene.attach_mesh("link_tcp", "tandenborstel", touch_links=touch_links)
        rospy.sleep(1)


    def verwijder_tandenborstel_mesh(self):
        self.scene.remove_attached_object("link_tcp", name="tandenborstel")
        rospy.sleep(1)

        self.scene.remove_world_object("tandenborstel")
        rospy.sleep(1)




    def foutafhandeling(self):
        self.result.tandenborstel_gesorteerd = False
        self.action_server.set_aborted(self.result)
        self.verwijder_tandenborstel_mesh()
        self.gripper_openen() 
        self.gripper_uitschakelen()

if __name__ == "__main__":
    rospy.init_node('manipulator_node')
    manipulator = unit_manipulator()
    rospy.spin()
