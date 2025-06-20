#!/usr/bin/env python
import rospy
import sys
import moveit_commander
from std_msgs.msg import Int32   
from xarm_msgs.srv import SetInt16
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
            # bak0
            0: ((0.061, 0.262, 0.226), (0.749, 0.660, 0.057, -0.013)), 
            # bak1
            1: ((0.185, 0.231, 0.226), (0.675, 0.738, 0, 1)),
            # bak2
            2: ((0.185, 0.231, 0.226), (0.675, 0.738, 0, 1)),
            # bak3
            3: ((0.185, 0.231, 0.226), (0.675, 0.738, 0, 1)),
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
        self.transformeren()

        # self.gripper_openen()
        self.naar_tandenborstel()
        # self.gripper_sluiten()

        self.feedback.tandenborstel_opgepakt = True  
        self.action_server.publish_feedback(self.feedback)

        self.naar_sorteerbak(self.type_tandenborstel)
        # self.gripper_openen()

        self.result.tandenborstel_gesorteerd = True
        self.action_server.set_succeeded(self.result)



    def positie_callback(self, msg):
        self.positie_object_vanuit_camera = msg
    
    def type_callback(self, msg):
        self.type_tandenborstel = msg.data

    def transformeren(self):
        transform = self.tf_buffer.lookup_transform('link_base',self.positie_object_vanuit_camera.header.frame_id,rospy.Time(0),
            rospy.Duration(1.0))
        self.positie_object_vanuit_base = do_transform_pose(self.positie_object_vanuit_camera, transform)

    def naar_tandenborstel(self):
        self.group.set_start_state_to_current_state()  # belangrijk!
        self.group.set_pose_target(self.positie_object_vanuit_base)
        self.group.go(wait=True)
        self.group.clear_pose_targets()       

    def naar_sorteerbak(self, type_tandenborstel):
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
        self.group.go(wait=True)
        self.group.clear_pose_targets()

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

    

if __name__ == "__main__":
    rospy.init_node('manipulator_node')
    manipulator = unit_manipulator()
    rospy.spin()
