#!/usr/bin/env python
import rospy
import sys
import moveit_commander
from geometry_msgs.msg import PoseStamped

rospy.init_node('check_pose')
group = moveit_commander.MoveGroupCommander('arm')
pose = group.get_current_pose().pose

print("{:.4f} , {:.4f} , {:.4f}".format(pose.position.x, pose.position.y, pose.position.z))
print("{:.4f} ,{:.4f} ,{:.4f} , {:.4f}".format(pose.orientation.x, pose.orientation.y, pose.orientation.z, pose.orientation.w))
