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


class unit_manipulator:
    def __init__(self):
        #positie object t.o.v. camera assenstelsel
        self.positie_object_vanuit_camera = None
        #getransformeerde coordinaten
        self.positie_object_vanuit_base = None
        self.type_tandenborstel = None
        #getal waarmee gripper kan worden gesloten
        self.GRIPPER_DICHT = 0
        #getal waarmee gripper kan worden geopend
        self.GRIPPER_OPEN = 1

        self.posities_sorteerbakken = {
            # bak1
            0: ((-0.2186, 0.2695, 0.1484), (-0.7491, -0.6599, -0.0574,0.0130)), 
            # bak2
            1: ((-0.2113 , 0.2005 , 0.0625), (-0.8069 ,-0.5821 ,-0.0822 , 0.0583)),
            # bak3
            2: ((-0.1259 , 0.3191 , 0.1596), (-0.6286 ,-0.7171 ,-0.2482 , 0.1704)),
            # bak4
            3: ((-0.1200 , 0.1957 , 0.0698), (-0.6779 ,-0.7206 ,-0.1454 , 0.0093)),
        }

        moveit_commander.roscpp_initialize(sys.argv)
        self.robot = moveit_commander.RobotCommander()
        self.scene = moveit_commander.PlanningSceneInterface()
        self.group = moveit_commander.MoveGroupCommander('arm')
        # self.group.set_max_velocity_scaling_factor(0.01)      
        # self.group.set_max_acceleration_scaling_factor(0.02)

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

    def start_manipulator(self, request):   
        if self.positie_object_vanuit_camera is None or self.type_tandenborstel is None:
            rospy.logerr("Ontbrekende gegevens: positie of type tandenborstel is nog niet ontvangen van visionsysteem.")
            self.foutafhandeling()
            return

        if not self.transformeren():
            self.foutafhandeling()
            return  # Stop bij fouten in transformeren

        # self.gripper_openen()  # Optioneel gripper openen, nu uitgeschakeld

        if not self.naar_tandenborstel():
            self.foutafhandeling()
            return  # Stop als bewegen naar tandenborstel mislukt

        # self.gripper_sluiten()  # Optioneel gripper sluiten, nu uitgeschakeld

        self.feedback.tandenborstel_opgepakt = True
        self.action_server.publish_feedback(self.feedback)

        if not self.naar_sorteerbak(self.type_tandenborstel):
            self.foutafhandeling()
            return  # Stop als bewegen naar sorteerbak mislukt

        # self.gripper_openen()  # Optioneel gripper openen bij sorteerbak, nu uitgeschakeld

        self.result.tandenborstel_gesorteerd = True
        self.action_server.set_succeeded(self.result)

        # Gripper uitzetten aan het einde
        # if not self.gripper_uit():
        #     self.foutafhandeling()
        #     return



    def positie_callback(self, msg):
        self.positie_object_vanuit_camera = msg
    
    def type_callback(self, msg):
        self.type_tandenborstel = msg.data

    def transformeren(self):
        try:
            transform = self.tf_buffer.lookup_transform('link_base', self.positie_object_vanuit_camera.header.frame_id, 
            rospy.Time(0), rospy.Duration(1.0))
            self.positie_object_vanuit_base = do_transform_pose(self.positie_object_vanuit_camera, transform)
            return True
        except (tf2_ros.LookupException, tf2_ros.ConnectivityException, tf2_ros.ExtrapolationException) as e:
            rospy.logerr("error bij transformeren: "+ str(e))
            return False
            

    def naar_tandenborstel(self):
        try:
            self.group.set_start_state_to_current_state()  # belangrijk!
            self.group.set_pose_target(self.positie_object_vanuit_base)
            success = self.group.go(wait=True)
            self.group.clear_pose_targets()

            if not success:
                rospy.logerr("Bewegen naar tandenborstel mislukt")
                return False

            return success
        except Exception as e:
            rospy.logerr("error bij het bewegen richting de tandenborstel: "+ str(e))  
            return False

    def naar_sorteerbak(self, type_tandenborstel):
        try: 
            positie, orientatie = self.posities_sorteerbakken[type_tandenborstel]
            pose_target = Pose()
            pose_target.position.x = positie[0]
            pose_target.position.y = positie[1]
            pose_target.position.z = positie[2]
            pose_target.orientation.x = orientatie[0]
            pose_target.orientation.y = orientatie[1]
            pose_target.orientation.z = orientatie[2]
            pose_target.orientation.w = orientatie[3]

            self.group.set_start_state_to_current_state()  # belangrijk!
            self.group.set_pose_target(pose_target)
            success = self.group.go(wait=True)
            self.group.clear_pose_targets()

            if not success:
                rospy.logerr("Bewegen naar sorteerbak mislukt")
                return False

            return success
        except Exception as e:
            rospy.logerr("error bij het bewegen richting sorteerbak "+ str(type_tandenborstel+1) + str(e))    
            return False  

    def gripper_openen(self):
        rospy.wait_for_service('/ufactory/vacuum_gripper_set')
        gripper = rospy.ServiceProxy('/ufactory/vacuum_gripper_set', SetInt16)
        resp = gripper(self.GRIPPER_OPEN)

        # toegestane_timeout = 5  # seconden
        # start = time.time()

        # while resp.ret != self.GRIPPER_OPEN:
        #     if time.time() - start > toegestane_timeout:
        #         rospy.logerr("Fout: Gripper opent niet!")
        #         break
        #     time.sleep(0.01)
    
    def gripper_sluiten(self):
        rospy.wait_for_service('/ufactory/vacuum_gripper_set')
        gripper = rospy.ServiceProxy('/ufactory/vacuum_gripper_set', SetInt16)
        resp = gripper(self.GRIPPER_DICHT)

    def gripper_uit(self):
        try: 
            rospy.wait_for_service('/ufactory/stop_lite6_gripper')
            gripper = rospy.ServiceProxy('/ufactory/stop_lite6_gripper', Call)
            resp = gripper()
            return True
        except rospy.ServiceException as e:
            rospy.logwarn("Uitschakelen van gripper faalde: "+ str(e))
            return False

    def foutafhandeling(self):
        self.result.tandenborstel_gesorteerd = False
        self.action_server.set_aborted(self.result)

if __name__ == "__main__":
    rospy.init_node('manipulator_node')
    manipulator = unit_manipulator()
    rospy.spin()
