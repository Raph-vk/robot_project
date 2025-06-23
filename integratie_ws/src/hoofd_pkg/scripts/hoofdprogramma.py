#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Type: Programma
Naam programma: hoofdprogramma.py

Programmeur 1: Raph van Koeveringe
Programmeurnummer: 2218115

Vak: Robotica in de machinebouw
Locatie: Breda
Datum: 19-6-2025
Versie: 1.1

Functionele beschrijving:
Hoofdfunctie:


Deelfuncties:

'''

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
from xarm_msgs.srv import ClearErr

# Actionlib
import actionlib

# Custom action messages
from robotarm.msg import manipulatorAction, manipulatorGoal, manipulatorFeedback, manipulatorResult
from transportsysteem_pkg.msg import TransportControlAction, TransportControlGoal, TransportControlFeedback, TransportControlResult

class hoofdprogramma:
    
    # Initialize the controller
    def __init__(self):        
        # Interne Toestanden stellen
        self.state = "WACHTEN_OP_START" # opties: "WACHTEN_OP_START", "IN_BEDRIJF", "ERROR", "FOUT" 
        
        # Button state
        self.start_pressed = False
        self.start_continue_pressed = False
        self.stop_pressed = False
        self.reset_pressed = False
        self.noodstop_voldaan = False

        # HMI-status publisher
        self.hmi_pub = rospy.Publisher('/hmi/status', String, queue_size=1)

        # Subscribers for buttons
        self.start = rospy.Subscriber('/start', Bool, self.start_callback)
        self.start_continue   = rospy.Subscriber('/start_continue', Bool, self.start_continue_callback)
        self.stop = rospy.Subscriber('/stop', Bool, self.stop_callback)
        self.reset   = rospy.Subscriber('/reset',   Bool, self.reset_callback)

        # Emergency topics
        self.noodstop_ingedrukt = rospy.Subscriber('/Noodstop_aan', Bool, self.noodstop_callback)
        self.noodstop_afgehandeld = rospy.Subscriber('/Noodstop_afgehandeld', Bool, self.noodstop_voldaan_callback)
        rospy.wait_for_service('/ufactory/moveit_clear_err')
        self.noodstop_uit = rospy.ServiceProxy('/ufactory/moveit_clear_err', ClearErr)

        # Action client
        self.transport_client = actionlib.SimpleActionClient('/transport_control', TransportControlAction)
        rospy.loginfo("Waiting for transportsysteem action server...")
        self.transport_client.wait_for_server(rospy.Duration(30))
        rospy.loginfo("Connected to transportsysteem action server.")

        # wachten tot Vision service beschikbaar is.
        rospy.wait_for_service('/vision')
        rospy.loginfo("Waiting for vision service server...")
        self.vision = rospy.ServiceProxy('/vision', SetBool)
        rospy.loginfo("Connected to vision service server.")
        
        # Action Client
        self.manipulator_client = actionlib.SimpleActionClient('manipulator_action', manipulatorAction)
        rospy.loginfo("Waiting for manipulator action server...")
        self.manipulator_client.wait_for_server(rospy.Duration(30))
        rospy.loginfo("Connected to manipulator action server.")

        #State machine oproepen
        self.state_machine()


    # ================= Knoppen CALLBACK FUNCTIES ======================
    def start_callback(self, msg):
        rospy.loginfo("Start button pressed: %s", msg.data)

        if msg.data and not self.start_pressed:
            rospy.loginfo("Start button pressed.")
            self.start_pressed = True

    def start_continue_callback(self, msg):
        rospy.loginfo("Start/Continue button pressed: %s", msg.data)
        self.start_continue_pressed = msg.data

    def stop_callback(self, msg):
        rospy.logwarn("Stop button pressed: %s", msg.data)
        self.stop_pressed = msg.data

    def reset_callback(self, msg):
        rospy.loginfo("Reset button pressed: %s", msg.data)    
        self.reset_pressed = msg.data

    def noodstop_callback(self, msg):
        rospy.logwarn("Emergency button pressed: %s", msg.data)    
        self.noodstop_pressed = msg.data
        self.state = "ERROR"

    def noodstop_voldaan_callback(self, msg):
        rospy.logwarn("Noodstop proces is voldaan, reset is mogelijk")    
        self.noodstop_voldaan = msg.data

    def feedback_manipulator_callback(self, feedback):

        if manipulator.feedback:
            rospy.loginfo("Object is opgepakt")

            #Transportsysteem start-commando versturen
            rospy.loginfo("Startcommando naar transportsysteem")
            goal = TransportControlGoal()
            goal.instruction = "start"
            self.transport_client.send_goal(goal)
            rospy.loginfo("start goal is verzonden naar transportsysteem")


    # === STATE METHODS ===
    def state_wachten_op_start(self):
        self.hmi_pub.publish("WACHTEN_OP_START")
        if self.start_pressed:
            self.start_pressed = False
            self.state = "TRANSPORTSYSTEEM"

        if self.start_pressed:

    def state_transport(self):
        self.hmi_pub.publish("IN_BEDRIJF")
        rospy.loginfo("Transportfase gestart")
        goal = TransportControlGoal(instruction="start")
        self.transport_client.send_goal(goal)
        self.transport_client.wait_for_result()
        result = self.transport_client.get_result()

        if result and result.result:
            rospy.loginfo("Transport succesvol")
            self.state = "VISION"
        else:
            rospy.logwarn("Transport mislukt")
            self.state = "FOUT"

    def state_vision(self):
        self.hmi_pub.publish("IN_BEDRIJF")
        try:
            request = SetBoolRequest(data=True)
            response = self.vision(request)
            if response.success:
                rospy.loginfo("Vision succesvol: %s", response.message)
                self.state = "MANIPULATOR"
            else:
                rospy.logwarn("Vision fout: %s", response.message)
                self.state = "FOUT"
        except rospy.ServiceException as e:
            rospy.logerr("Service call vision faalde: %s", e)
            self.state = "FOUT"

    def state_manipulator(self):
        self.hmi_pub.publish("IN_BEDRIJF")
        goal = manipulatorGoal(manipulator_start=True)
        self.manipulator_client.send_goal(goal)
        self.manipulator_client.wait_for_result()
        result = self.manipulator_client.get_result()

        if result and result.tandenborstel_gesorteerd:
            rospy.loginfo("Manipulatie succesvol")
            self.state = "WACHTEN_OP_START"
        else:
            rospy.logwarn("Manipulatie mislukt")
            self.state = "FOUT"

    def state_fout(self):
        self.hmi_pub.publish("FOUT")
        rospy.loginfo("In FOUT state")
        self.start_continue_pressed = False
        self.start_pressed = False

        if self.reset_pressed:
            rospy.loginfo("Reset knop ingedrukt")
            self.reset_pressed = False
            self.state = "WACHTEN_OP_START"

    def state_error(self):
        self.hmi_pub.publish("ERROR")
        rospy.loginfo("In ERROR state")
        self.start_continue_pressed = False
        self.start_pressed = False

        if self.reset_pressed and self.noodstop_voldaan:
            rospy.loginfo("Reset knop ingedrukt")
            self.noodstop_uit()
            self.reset_pressed = False
            self.state = "WACHTEN_OP_START"

    # === STATE MACHINE LOOP ===
    def state_machine(self):
        rospy.loginfo("State machine gestart")
        rate = rospy.Rate(10)
        while not rospy.is_shutdown():
            if self.state == "WACHTEN_OP_START":
                self.state_wachten_op_start()
            elif self.state == "TRANSPORTSYSTEEM":
                self.state_transport()
            elif self.state == "VISION":
                self.state_vision()
            elif self.state == "MANIPULATOR":
                self.state_manipulator()
            elif self.state == "FOUT":
                self.state_fout()
            elif self.state == "ERROR":
                self.state_error()
            else:
                rospy.logwarn("Onbekende state: %s", self.state)
                self.state = "FOUT"
            rate.sleep()


if __name__ == '__main__':
    rospy.loginfo("hoofdprogramma node wordt gestart.")
    rospy.init_node('hoofdprogramma_node')
    
    try:
        hoofdprogramma()
    except rospy.ROSInterruptException:
        pass