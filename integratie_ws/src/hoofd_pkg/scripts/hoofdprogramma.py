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
from transportsysteem_pkg.msg import TransportControlAction, TransportControlGoal, TransportControlFeedback, TransportControlResult

class hoofdprogramma:

    # Initialize the controller
    def __init__(self):
        rospy.init_node('hoofdprogramma_node')       # Initialize the ROS node.
        
        # Toestanden
        self.stap = "IDLE"
        self.state = "IDLE"


        # Button state
        self.start_pressed = False
        self.start_continue_pressed = False
        self.stop_pressed = False
        self.reset_pressed = False

        # Subscribers for buttons
        self.start = rospy.Subscriber('/start', Bool, self.start_callback)
        self.start_continue   = rospy.Subscriber('/start_continue', Bool, self.start_continue_callback)
        self.stop = rospy.Subscriber('/stop', Bool, self.stop_callback)
        self.reset   = rospy.Subscriber('/reset',   Bool, self.reset_callback)
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

        # Timer die elke 0.5 seconden de state-machine draait
        self.timer = rospy.Timer(rospy.Duration(0.5), self.state_machine)

    # ================= Knoppen CALLBACK FUNCTIES ======================
    def start_callback(self, msg):
        rospy.loginfo("Start button pressed: %s", msg.data)
        start_pressed = msg.data
        self.cyclus(None)

    def start_continue_callback(self, msg):
        rospy.loginfo("Start/Continue button pressed: %s", msg.data)
        start_continue_pressed = msg.data

    def stop_callback(self, msg):
        rospy.loginfo("Stop button pressed: %s", msg.data)
        stop_pressed = msg.data

    def reset_callback(self, msg):
        rospy.loginfo("Reset button pressed: %s", msg.data)    
        reset_pressed = msg.data

 # ================= STATE MACHINE LOOP ======================
    def state_machine(self, event):
        if self.state == "IDLE":
            self.rood.publish(True)
            self.oranje.publish(False)
            self.groen.publish(False)

            if self.start_pressed:
                rospy.loginfo("Overgang naar STARTEN")
                self.state = "STARTEN"
                self.start_pressed = False
        
        elif self.state == "STARTEN":
            rospy.loginfo("Startcommando naar transportsysteem")
            goal = TransportControlGoal()
            goal.command = "start"
            self.transport_client.send_goal(goal)
            self.state = "WACHTEN"

        elif self.state == "WACHTEN":
            self.rood.publish(False)
            self.oranje.publish(True)
            self.groen.publish(False)

            # Voorbeeld van conditie om naar RUNNING te gaan
            if self.start_continue_pressed:
                rospy.loginfo("Doorgaan met volgende stap")
                self.state = "RUNNING"
                self.start_continue_pressed = False

        elif self.state == "RUNNING":
            self.rood.publish(False)
            self.oranje.publish(False)
            self.groen.publish(True)

            rospy.loginfo("Systeem is actief.")
            # Hier kan extra logica komen voor actieve processen

        if self.reset_pressed:
            rospy.loginfo("Reset ontvangen, terug naar IDLE")
            self.state = "IDLE"
            self.reset_pressed = False


if __name__ == '__main__':
    
    node = hoofdprogramma()
    rospy.spin()