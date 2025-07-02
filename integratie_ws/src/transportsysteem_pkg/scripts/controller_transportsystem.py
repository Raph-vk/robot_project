#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Type: Script
Naam programma: controller_transportsysteem.py

Programmeur 1: Raph van Koeveringe
Programmeurnummer: 2218115

Vak: Robotica in de machinebouw
Locatie: Breda
Datum: 19-6-2025
Versie: 1.1

Functionele beschrijving:
Het aansturen van het transportsysteem via een action server. 
Er is een 'start'-cyclus om het product naar de robotcel te transporteren.
Er is ook een 'dump'-cyclus om een foutief product te deponeren

Hoofdfunctie:
    - Handlecontrole om de instructie-cyclus te verwerken

Deelfuncties:
    - Callback functies voor de sensoren
'''
import rospy                                      # ROS Python client library
import actionlib
from std_msgs.msg import Bool                     # For publishing motor on/off
from transportsysteem_pkg.msg import TransportControlAction, TransportControlFeedback, TransportControlResult

class TransportController:

    # Initialize the controller
    def __init__(self):
        rospy.init_node('transport_control_node')       # Initialize the ROS node.
        # Publisher to send True/False to /motor_command
        self.motor_pub = rospy.Publisher('/motor_command', Bool, queue_size=1)
        # Subscribers for the two IR beam topics
        self.ir_begin_sub = rospy.Subscriber('/ir_begin', Bool, self._ir_begin_cb)
        self.ir_end_sub   = rospy.Subscriber('/ir_end',   Bool, self._ir_end_cb)
        # Internal flags to hold latest IR readings
        self.ir_begin = False
        self.ir_end   = False
        # State: one of 'idle', 'start', or 'dump'
        self.state = 'idle'

        # Create action server
        self._as = actionlib.SimpleActionServer('transport_control', TransportControlAction, self._handle_control, True)
        rospy.loginfo("TransportControlAction server started.")


    # ==== CALLBACK FUNCTIES ====
    def _ir_begin_cb(self, msg):
        self.ir_begin = msg.data                     # Update begin‐sensor flag

    def _ir_end_cb(self, msg):
        self.ir_end = msg.data                       # Update end‐sensor flag

    # Handle the instructions
    def _handle_control(self, req):
        result   = TransportControlResult()
        instructie = req.instruction.strip().lower()
        rate = rospy.Rate(10)

        # start cyclus
        if instructie == 'start':            
            rospy.loginfo("Start sequence initiated")

            # Als er al een product op eindpositie is
            if self.ir_end:
                rospy.loginfo("Product staat al op eindpositie.")
                if self._as.is_active():
                    result.gelukt = True
                    result.bericht = "Product onder vision camera."
                    self._as.set_succeeded(result)
                return
            rospy.loginfo("Nog geen product op eindpostie")

            # Loopen tot een object bij begin positie is.
            rospy.loginfo("Wachten op object op begin positie...")
            while not rospy.is_shutdown() and not self.ir_begin:
                rate.sleep()

            # Motor starten
            rospy.loginfo("Object detected, running motor")
            self.motor_pub.publish(Bool(data=True))

            # Wacht tot er een object bij eindpositie is
            start_time = rospy.Time.now()
            while not rospy.is_shutdown() and not self.ir_end:

                # Stop whileloop als het langer dan 20sec duurt.
                if (rospy.Time.now() - start_time).to_sec() > 20.0:
                    rospy.logerr("Timeout: object bereikte de eind-sensor niet, binnen gestelde tijd.")
                    self.motor_pub.publish(Bool(data=False))
                    result.gelukt = False
                    result.bericht = "Timeout: object bereikte de eind-sensor niet, binnen gestelde tijd."
                    return self._as.set_succeeded(result)
                rate.sleep()

            # Met kleine delay motor uitzetten en resultaat delen
            rospy.sleep(0.75)
            self.motor_pub.publish(Bool(data=False))
            rospy.loginfo("Reached end, stopping motor")
            result.gelukt = True
            result.bericht = "Product is aangekomen op eindpositie."
            self._as.set_succeeded(result)

        # Dump cyclus
        elif instructie == 'dump':
            rospy.loginfo("Dump: dumping product.")

            # Result false als er geen object voor sensor is.
            if not self.ir_end:
                rospy.logerr("Geen product op eindpositie gedetecteerd.")
                result.gelukt = False
                result.bericht = "Geen product gedetecteerd om te dumpen."
                self._as.set_succeeded(result)
                return

            # Motor inschakelen
            self.motor_pub.publish(Bool(data=True))

            # Wacht tot object sensor verlaten heeft.
            start_time = rospy.Time.now()
            while not rospy.is_shutdown() and self.ir_end:

                # Stop whileloop als het langer dan 10sec duurt.
                if (rospy.Time.now() - start_time).to_sec() > 10.0:
                    rospy.logerr("Timeout: object bereikte de eind-sensor niet, binnen gestelde tijd.")
                    self.motor_pub.publish(Bool(data=False))
                    result.gelukt = False
                    result.bericht = "Timeout: object bereikte de eind-sensor niet, binnen gestelde tijd."
                    return self._as.set_succeeded(result)
                rate.sleep()
            rospy.loginfo("Product is verdwenen voor de sensor.")

            # Blijf nog even draaien voor de zekerheid en stop de motor
            rospy.sleep(5.0)
            self.motor_pub.publish(Bool(data=False))
            rospy.loginfo("Motor gestopt, dump is succesvol.")

            # Publiseer dat gelukt is
            result.gelukt = True
            result.bericht = "Dump sequence complete"
            self._as.set_succeeded(result)

        # Als er een onbekende instructie ontvangen wordt, Fout
        else:
            result.gelukt   = False
            result.bericht = "onbekende instructie"
            self._as.set_aborted(result)

if __name__ == '__main__':
    node = TransportController()
    rospy.spin()