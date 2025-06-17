#!/usr/bin/env python
import rospy
import sys
import moveit_commander
from geometry_msgs.msg import Pose

def main():
    rospy.init_node('simple_move_node')

    moveit_commander.roscpp_initialize(sys.argv)
    group = moveit_commander.MoveGroupCommander('arm')

    rospy.sleep(2)  # wachten tot alles klaar is

    group.set_start_state_to_current_state()

    target_pose = Pose()
    target_pose.position.x = 0.185
    target_pose.position.y = 0.231
    target_pose.position.z = 0.226

    # Identity quaternion: geen rotatie
    target_pose.orientation.x = 0.0
    target_pose.orientation.y = 0.0
    target_pose.orientation.z = 0.0
    target_pose.orientation.w = 1.0

    group.set_pose_target(target_pose)

    rospy.loginfo("Beweeg naar positie (0.185, 0.231, 0.226) met identity orientatie...")
    success = group.go(wait=True)

    group.clear_pose_targets()

    if success:
        rospy.loginfo("Beweging gelukt!")
    else:
        rospy.logerr("Beweging mislukt!")

if __name__ == '__main__':
    main()
