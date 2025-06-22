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
Versie: 1.0

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

        # HMI-status publisher
        self.hmi_pub = rospy.Publisher('/hmi/status', String, queue_size=1)

        # Subscribers for buttons
        self.start = rospy.Subscriber('/start', Bool, self.start_callback)
        self.start_continue   = rospy.Subscriber('/start_continue', Bool, self.start_continue_callback)
        self.stop = rospy.Subscriber('/stop', Bool, self.stop_callback)
        self.reset   = rospy.Subscriber('/reset',   Bool, self.reset_callback)

        # Emergency topics
        self.noodstop_ingedrukt = rospy.Subscriber('/Noodstop_aan', Bool, self.noodstop_callback)
        self.noodstop_afgehandeld = rospy.Subscriber('/Noodstop_afgehandeld', Bool, self.start_continue_callback)

        # Action client
        self.transport_client = actionlib.SimpleActionClient('/transport_control', TransportControlAction)
        rospy.loginfo("Waiting for transportsystem action server...")
        self.transport_client.wait_for_server(rospy.Duration(30))
        rospy.loginfo("Connected to transportsystem action server.")

        # wachten tot Vision service beschikbaar is.
        rospy.wait_for_service('/vision')
        rospy.loginfo("Waiting for vision service server...")
        self.vision = rospy.ServiceProxy('/vision', SetBool)
        rospy.loginfo("Connected to vision service server.")
        
        #State machine oproepen
        self.state_machine()


    # ================= Knoppen CALLBACK FUNCTIES ======================
    def start_callback(self, msg):
        #rospy.loginfo("Start button pressed: %s", msg.data)
        #self.start_pressed = msg.data
        #self.state = "IN_BEDRIJF"
        if msg.data and not self.start_pressed:
            rospy.loginfo("Start button pressed.")
            self.start_pressed = True

    def start_continue_callback(self, msg):
        rospy.loginfo("Start/Continue button pressed: %s", msg.data)
        self.start_continue_pressed = msg.data
        #self.state = "IN_BEDRIJF"

    def stop_callback(self, msg):
        rospy.logwarn("Stop button pressed: %s", msg.data)
        self.stop_pressed = msg.data

    def reset_callback(self, msg):
        rospy.loginfo("Reset button pressed: %s", msg.data)    
        self.reset_pressed = msg.data
        #self.state = "WACHTEN_OP_START"

    def noodstop_callback(self, msg):
        rospy.logwarn("Emergency button pressed: %s", msg.data)    
        self.noodstop_pressed = msg.data
        self.state = "ERROR"

    def noodstop_voldaan_callback(self, msg):
        rospy.logwarn("Noodstop proces is voldaan, reset is mogelijk")    
        self.noodstop_voldaan = msg.data



 # ================= STATE MACHINE LOOP ==========================
    def state_machine(self):
        rospy.loginfo("state_machine draait")
        rate = rospy.Rate(10)  # 10 Hz

        while not rospy.is_shutdown():
            # --- WACHTEN OP START status ---
            if self.state == "WACHTEN_OP_START":
                self.hmi_pub.publish("WACHTEN_OP_START")

                if self.start_pressed:
                    rospy.loginfo("Overgang naar IN_BEDRIJF")
                    self.state = "IN_BEDRIJF"
                    self.start_pressed = False #startknop resetten naar false
        
            # ------- IN BEDRIJF status --- dus aftelopen cyclus -----
            elif self.state == "IN_BEDRIJF":
                self.hmi_pub.publish("IN_BEDRIJF")
                rospy.loginfo("in IN_BEDRIJF state")

                #Transportsysteem start-commando openen
                rospy.loginfo("Startcommando naar transportsysteem")
                goal = TransportControlGoal()
                goal.instruction = "start"
                self.transport_client.send_goal(goal)
                rospy.loginfo("start goal is verzonden naar transportsysteem")

                # resultaat vanuit transportsysteem is TRUE.
                self.transport_client.wait_for_result()  # Wacht tot klaar
                transport = self.transport_client.get_result()  # Resultaat ophalen
                rospy.loginfo("Resultaat van transportsysteem ontvangen")

                if transport.result:
                    rospy.loginfo("Transport succesvol gelukt.") #result = true
                else:
                    rospy.logwarn("Transport mislukt.") #result = false
                    self.state = "FOUT"

                #Vision start-commando openen # SetBool service aanroepen met expliciete True
                try:
                    rospy.loginfo("Service '/vision' wordt aangeroepen met TRUE...")
                    request = SetBoolRequest()
                    request.data = True  # ← hier stuur je echt True

                    # terugkoppeling uitlezen
                    response = self.vision(request)  # response bevat: success + message
                    if response.success:
                        rospy.loginfo("Service succesvol: {}".format(response.message))
                    else:
                        rospy.logwarn("Service fout: {}".format(response.message))
                        self.state = "FOUT"
                except rospy.ServiceException as e:
                    rospy.logerr("Service call naar '/vision' faalde: {}".format(e))
                    self.state = "FOUT"
                
                self.state = "WACHTEN_OP_START"

            # ------- ERROR status --- dus noodstop ingedrukt of crash -----
            elif self.state == "ERROR":
                self.hmi_pub.publish("ERROR")
                rospy.loginfo("in ERROR state")

                self.start_continue_pressed = False
                self.start_pressed = False

                # Resetknop indrukken
                if self.reset_pressed and noodstop_voldaan:
                    rospy.loginfo("Reset knop ingedrukt")
                    self.state = "WACHTEN_OP_START"
                    self.reset_pressed = False

            # ------- FOUT status --- false als result teruggekregen -----
            elif self.state == "FOUT":
                self.hmi_pub.publish("FOUT")
                rospy.loginfo("in FOUT state")

                self.start_continue_pressed = False
                self.start_pressed = False

                # Resetknop indrukken
                if self.reset_pressed:
                    rospy.loginfo("Reset knop ingedrukt")
                    self.state = "WACHTEN_OP_START"
                    self.reset_pressed = False

            # ------- else ------
            else:
                self.hmi_pub.publish("FOUT")
                rospy.loginfo("in FOUT state")

                self.start_continue_pressed = False
                self.start_pressed = False

                # Resetknop indrukken
                if self.reset_pressed:
                    rospy.loginfo("Reset knop ingedrukt")
                    self.state = "WACHTEN_OP_START"
                    self.reset_pressed = False
        
            rate.sleep()

if __name__ == '__main__':
    rospy.loginfo("hoofdprogramma node wordt gestart.")
    rospy.init_node('hoofdprogramma_node')       # Initialize the ROS node.
    
    
    try:
        hoofdprogramma()
    except rospy.ROSInterruptException:
        pass