#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Type: Script
Naam programma: hoofdprogramma.py

Programmeur 1: Raph van Koeveringe
Programmeurnummer: 2218115

Vak: Robotica in de machinebouw
Locatie: Breda
Datum: 19-6-2025
Versie: 1.1

Functionele beschrijving:
Het plaatsen van het systeem naar verschillende statussen en aansturen van deel systemen.

Hoofdfunctie:
    - Statemachine

Deelfuncties:
    - Callback functies van iedeere drukknop
    - Callback functies van continuemode of feedback vanuit manipulator
    - Statussen aansturing
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

# For robot init location
import moveit_commander
import sys
from geometry_msgs.msg import Pose, Point, Quaternion

class hoofdprogramma:
    
    # Initialize the controller
    def __init__(self):        
        # Interne Toestanden stellen
        self.state = "INITIALISATIE" # opties: "WACHTEN_OP_START", "IN_BEDRIJF", "ERROR", "FOUT" 
        
        # Button state
        self.start_pressed = False
        self.start_continue_pressed = False
        self.stop_pressed = False
        self.reset_pressed = False
        self.noodstop_pressed = False
        self.noodstop_voldaan = False
        self.noodstop_is_uit = False

        #Variable state
        self.continue_mode = False

        # HMI-status publisher
        self.hmi_pub = rospy.Publisher('/hmi/status', String, queue_size=1)
        self.continue_mode_pub = rospy.Publisher('/continue_mode', Bool, queue_size=1)

        # Subscribers for buttons
        self.start = rospy.Subscriber('/start', Bool, self.start_callback)
        self.start_continue = rospy.Subscriber('/start_continue', Bool, self.start_continue_callback)
        self.stop = rospy.Subscriber('/stop', Bool, self.stop_callback)
        self.reset = rospy.Subscriber('/reset', Bool, self.reset_callback)

        # Subscriben van ir eindsensor
        self.ir_end_sub   = rospy.Subscriber('/ir_end',   Bool, self._ir_end_cb)

        # Emergency topics
        self.noodstop_ingedrukt = rospy.Subscriber('/Noodstop_aan', Bool, self.noodstop_callback)
        self.noodstop_uitgerukt = rospy.Subscriber('/Noodstop_uit', Bool, self.noodstop_uitgerukt_callback)
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

    # Startknop callback
    def start_callback(self, msg):
        rospy.loginfo("Start button pressed: %s", msg.data)

        if msg.data and not self.start_pressed:
            self.start_pressed = True

    # Start_continue knop callback
    def start_continue_callback(self, msg):
        rospy.loginfo("Start_Continue button pressed: %s", msg.data)
        
        if not self.state == "INITIALISATIE":
            self.start_continue_pressed = msg.data

            if msg.data and not self.continue_mode:
                self.continue_mode = True
                self.continue_mode_pub.publish(Bool(data=True))
                rospy.loginfo("Continue_mode aan")
            self.start_continue_pressed = False

    #Stop Callback functie
    def stop_callback(self, msg):
        rospy.logwarn("Stop button pressed: %s", msg.data)
        self.stop_pressed = msg.data
        if msg.data:
            self.continue_mode = False
            self.continue_mode_pub.publish(Bool(data=False))
            self.stop_pressed = False

    # Reset callback functie
    def reset_callback(self, msg):
        rospy.loginfo("Reset button pressed: %s", msg.data)    
        if msg.data:
            self.reset_pressed = msg.data

    # Noodstop callback
    def noodstop_callback(self, msg):
        if msg.data:
            rospy.logerr("Emergency button pressed: %s", msg.data)    
            rospy.logerr("Noodstop geactiveerd! Overschakelen naar ERROR state.")
            self.state = "ERROR"
            self.noodstop_pressed = True

    def noodstop_uitgerukt_callback(self, msg):
        self.noodstop_is_uit = msg.data

    def noodstop_voldaan_callback(self, msg):
        rospy.logwarn("Noodstop proces is voldaan, reset is mogelijk")    
        self.noodstop_voldaan = msg.data


    def _ir_end_cb(self, msg):
        self.ir_end = msg.data

    # Feedback manipulator verwerken
    def feedback_manipulator_callback(self, feedback):
        if self.continue_mode and feedback.tandenborstel_opgepakt:
            rospy.loginfo("Object is opgepakt, wachten tot robot weg is")
            
            # Wachten tot eindsensor uit gaat, dus robot weg
            while self.ir_end:
                rospy.sleep(0.5)

            # Start signaal naar transprotsysteem sturen
            rospy.loginfo("Robot is weg, start signaal naar transportband sturen")
            rospy.sleep(2)
            doel = TransportControlGoal(instruction="start")
            self.transport_client.send_goal(doel)
            rospy.loginfo("Transprot start Goal is verzonden vanuit feedback")

    # === STATE METHODS ===============================================

    # Initialisatie state methode
    def state_initialisatie(self):
        self.hmi_pub.publish("INITIALISATIE")

        # Druk start in om naar begin positie te gaan
        if self.start_pressed:
            self.start_pressed = False
            init_positie = ((-0.0345 , -0.2287 , 0.1078), (0.9436 ,-0.2732 ,0.1624 , 0.0926))

            # Instellingen en dergelijke robot
            moveit_commander.roscpp_initialize(sys.argv)
            robot = moveit_commander.RobotCommander()
            scene = moveit_commander.PlanningSceneInterface()
            group = moveit_commander.MoveGroupCommander('arm')
            group.set_max_velocity_scaling_factor(0.2)      
            group.set_max_acceleration_scaling_factor(0.05)
            group.set_num_planning_attempts(5)
            group.set_planning_time(10)

            # Orientatie en positie voor robot
            positie, orientatie = init_positie
            pose_target = Pose()
            pose_target.position.x = positie[0]
            pose_target.position.y = positie[1]
            pose_target.position.z = positie[2]
            pose_target.orientation.x = orientatie[0]
            pose_target.orientation.y = orientatie[1]
            pose_target.orientation.z = orientatie[2]
            pose_target.orientation.w = orientatie[3]

            # Plannen van positie
            group.set_start_state_to_current_state()
            group.set_pose_target(pose_target)
            plan = group.plan()
            
            # Controleer of plannen gelukt is
            if not plan or not plan.joint_trajectory.points:
                rospy.logerr("Plannen mislukt: geen trajectory gegenereerd")
                self.state = "FOUT"

            # Uitvoeren plan
            success = group.execute(plan, wait=True)
            group.clear_pose_targets()

            # Controleren of uitvoeren gelukt is
            if not success:
                rospy.logerr("Uitvoeren van plan mislukt")
                self.state = "FOUT"
            else:
                self.state = "WACHTEN_OP_START"
            self.start_continue_pressed=False
            self.stop_pressed=False
            self.reset_pressed=False

    # "Wachten op start" methode
    def state_wachten_op_start(self):
        self.hmi_pub.publish("WACHTEN_OP_START")

        # Als startknop ingedrukt wordt, ga naar transportsysteem
        if self.start_pressed:
            self.start_pressed = False
            self.state = "TRANSPORTSYSTEEM"
        elif self.continue_mode:
            self.state = "TRANSPORTSYSTEEM"

    # transportsysteem methode
    def state_transport(self):
        self.hmi_pub.publish("IN_BEDRIJF")

        rospy.loginfo("Transportfase gestart")
        doel = TransportControlGoal(instruction="start")
        self.transport_client.send_goal(doel)

        # Wacht tot resultaat verkregen wordt.
        self.transport_client.wait_for_result()
        result = self.transport_client.get_result()
        rospy.loginfo("Er ligt een object klaar onder vision-camera")

        # Bij geen resultaat ontvangen
        if result is None:
            rospy.logerr("Transport actie heeft geen resultaat teruggegeven (None).")
            self.state = "FOUT"
            return

        # Kijken of transport gelukt is of niet
        if result.gelukt:
            rospy.loginfo("Transport succesvol%s", result.bericht)
            self.state = "VISION"
        else:
            rospy.logerr("Transport mislukt: %s",result.bericht)
            self.state = "FOUT"

    # Vision code
    def state_vision(self):
        self.hmi_pub.publish("IN_BEDRIJF")
        rospy.loginfo("Vision start over paar seconden")
        rospy.sleep(3)
        rospy.loginfo("Vision gestart")

        # Voer vision uit en zet resultaat in "response"
        response = self.vision(SetBoolRequest(data=True))
        if response.success:
            rospy.loginfo("Vision succesvol: %s", response.message)
            self.state = "MANIPULATOR"
        else:
            rospy.logerr("Vision fout: %s", response.message)
            rospy.logwarn("Gaan product dumpen!!")

            # Als vision gefaald is voer dump functie uit.
            goal = TransportControlGoal(instruction="dump")
            self.transport_client.send_goal(goal)
            
            #Controleren of dump gelukt is
            self.transport_client.wait_for_result()
            dump_result = self.transport_client.get_result()
            if dump_result and dump_result.gelukt:
                rospy.loginfo("Dump succesvol%s", dump_result.bericht)
            else:
                rospy.logerr("Dump mislukt,%s", dump_result.bericht)
            self.state = "FOUT"
        
    # manipulator methode
    def state_manipulator(self):
        self.hmi_pub.publish("IN_BEDRIJF")

        #Stuur startsignaal naar manipulator
        goal = manipulatorGoal(manipulator_start=True)

        #Verstuur goal, inclusief feedback callback ernaast runnen.
        self.manipulator_client.send_goal(goal, feedback_cb=self.feedback_manipulator_callback)

        # Wacht op resultaat en verwerk
        self.manipulator_client.wait_for_result()
        result = self.manipulator_client.get_result()

        if result and result.tandenborstel_gesorteerd:
            rospy.loginfo("Manipulatie succesvol")
            self.state = "WACHTEN_OP_START"
        else:
            rospy.logerr("Uitsorteren van object mislukt")
            self.state = "FOUT"

    def state_fout(self):
        self.hmi_pub.publish("FOUT")
        self.start_continue_pressed = False
        self.start_pressed = False
        self.continue_mode = False
        self.stop_pressed=False

        # Na indrukken van resetknop ga naar initialisatie
        if self.reset_pressed:
            rospy.loginfo("Reset knop ingedrukt")
            self.reset_pressed = False
            self.state = "INITIALISATIE"

    def state_error(self):
        self.hmi_pub.publish("ERROR")
        self.start_continue_pressed = False
        self.start_pressed = False
        self.continue_mode = False
        self.stop_pressed=False

        # Als noodstop voldaan is, druk resetknop in.
        if self.reset_pressed and self.noodstop_voldaan:
            rospy.loginfo("Reset knop ingedrukt")

            while not self.noodstop_is_uit:
                rospy.logerr("Haal eerst noodstop eruit!!")
                self.noodstop_uit() # robot arm uit errorstate halen.
                rospy.sleep(0.5)
            self.reset_pressed = False
            self.noodstop_pressed = False
            self.noodstop_voldaan=False
            self.noodstop_is_uit=False
            self.state = "INITIALISATIE"

    # === STATE MACHINE LOOP ===
    def state_machine(self):
        rospy.loginfo("State machine gestart")
        rate = rospy.Rate(10)

        # Controleer welke state en activeer die functie
        while not rospy.is_shutdown():
            if self.noodstop_pressed or self.state == "ERROR":
                self.state_error()
            elif self.state == "FOUT":
                self.state_fout()
            elif self.state == "INITIALISATIE":
                self.state_initialisatie()
            elif self.state == "WACHTEN_OP_START":
                self.state_wachten_op_start()
            elif self.state == "TRANSPORTSYSTEEM":
                self.state_transport()
            elif self.state == "VISION":
                self.state_vision()
            elif self.state == "MANIPULATOR":
                self.state_manipulator()
            else:
                rospy.logerr("Onbekende state: %s", self.state)
                self.state = "FOUT"
            rate.sleep()


if __name__ == '__main__':
    rospy.loginfo("hoofdprogramma node wordt gestart.")
    rospy.init_node('hoofdprogramma_node')
    
    try:
        hoofdprogramma()
    except rospy.ROSInterruptException:
        pass