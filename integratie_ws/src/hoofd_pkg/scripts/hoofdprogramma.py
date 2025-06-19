#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy

# std_msgs
from std_msgs.msg import Int32
from std_msgs.msg import Bool
from std_msgs.msg import String
from std_msgs.msg import Header
from std_msgs.msg import Float32

# geometry_msgs
from geometry_msgs.msg import PoseStamped

# custom HMI messages
from std_msgs.msg import String as BesturingMsg  # assuming besturing.msg = String
from std_msgs.msg import String as SignaleringMsg  # assuming signalering.msg = String

# std_srvs
from std_srvs.srv import SetBool, SetBoolRequest, SetBoolResponse

# Actionlib
import actionlib

# Custom action messages
from robotarm.msg import manipulatorAction, manipulatorGoal, manipulatorFeedback, manipulatorResult
from transportsystem_pkg.msg import TransportControlAction, TransportControlGoal, TransportControlFeedback, TransportControlResult

class hoofdprogramma:

    # Initialize the controller
    def __init__(self):
        rospy.init_node('hoofdprogramma_node')       # Initialize the ROS node.
        
        # Button state
        self.start_pressed = False
        self.start_continue_pressed = False
        self.stop_pressed = False
        self.reset_pressed = False

        # Subscribers for buttons
        self.start = rospy.Subscriber('/start', Bool, lambda msg: rospy.loginfo("Start: %s", msg.data))
        self.start_continue   = rospy.Subscriber('/start_continue', Bool, lambda msg: rospy.loginfo("Start: %s", msg.data))
        self.stop = rospy.Subscriber('/stop', Bool, self.<fill_in>)
        self.reset   = rospy.Subscriber('/stop',   Bool, self.<fill_in>)
            # emergency is done in seperate script.

        # Publisher to send True/False to lamps
        self.rood = rospy.Publisher('/led_rood', Bool, queue_size=1)
        self.oranje = rospy.Publisher('/led_oranje', Bool, queue_size=1)
        self.groen = rospy.Publisher('/led_groen', Bool, queue_size=1)
    
        # Action client
        self.transport_client = actionlib.SimpleActionClient('/TransportControl', TransportControlAction)
        rospy.loginfo("Waiting for transportsystem action server...")
        self.transport_client.wait_for_server()
        rospy.loginfo("Connected to transportsystem action server.")

    # ================= Knoppen CALLBACK FUNCTIES ======================
    def start_callback(self, msg):
        rospy.loginfo("Start button pressed: %s", msg.data)
        start_pressed  = msg.data

    def start_continue_callback(self, msg):
        rospy.loginfo("Start/Continue button pressed: %s", msg.data)
        start_continue_pressed = msg.data

    def stop_callback(self, msg):
        rospy.loginfo("Stop button pressed: %s", msg.data)
        stop_pressed = msg.data

    def reset_callback(self, msg):
        rospy.loginfo("Reset button pressed: %s", msg.data)    
        reset_pressed = msg.data


    def cyclus(self, event):
        if self.start_pressed:
            goal = TransportControlGoal()
            goal.command = "start"
            #rospy.loginfo("Sending goal: start")
            self.transport_client.send_goal(goal)
            self.start_pressed = False  # Reset to prevent resending

if __name__ == '__main__':
    node = hoofdprogramma()
    rospy.spin()