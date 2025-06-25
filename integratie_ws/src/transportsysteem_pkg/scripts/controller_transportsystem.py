#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
        # State: one of 'idle', 'start', 'running_to_end', or 'dump'
        self.state = 'idle'

        # Create action server
        self._as = actionlib.SimpleActionServer(
            'transport_control',
            TransportControlAction,
            execute_cb=self._handle_control,
            auto_start=False
        )
        self._as.start()
        rospy.loginfo("TransportControlAction server started.")

    def _ir_begin_cb(self, msg):
        self.ir_begin = msg.data                     # Update begin‐sensor flag

    def _ir_end_cb(self, msg):
        self.ir_end = msg.data                       # Update end‐sensor flag
    

    # Handle the instructions
    def _handle_control(self, req):
        result   = TransportControlResult()
        instru = req.instruction.strip().lower()
        rate = rospy.Rate(10)

        if instru == 'start':            
            rospy.loginfo("Start sequence initiated")
            rospy.loginfo("Looking for object...")

            # wait for object at beginning
            while not rospy.is_shutdown() and not self.ir_begin:
                if self._as.is_preempt_requested():
                    return self._as.set_preempted()
                rate.sleep()

            rospy.loginfo("Object detected, running motor")
            self.motor_pub.publish(Bool(data=True))

            # wait for object at end, but give up after 20s
            start_time = rospy.Time.now()
            while not rospy.is_shutdown() and not self.ir_end:
                if self._as.is_preempt_requested():
                    return self._as.set_preempted()

                # timeout check
                if (rospy.Time.now() - start_time).to_sec() > 20.0:
                    rospy.logerr("Timeout: object bereikte de eind-sensor niet, binnen gestelde tijd.")
                    self.motor_pub.publish(Bool(data=False))
                    result.gelukt = False
                    result.bericht = "Timeout: object bereikte de eind-sensor niet, binnen gestelde tijd."
                    return self._as.set_succeeded(result)
                rate.sleep()

            rospy.sleep(0.75)
            self.motor_pub.publish(Bool(data=False))
            rospy.loginfo("Reached end, stopping motor")

            result.gelukt = True
            result.bericht = "Product is aangekomen op eindpositie."
            self._as.set_succeeded(result)

        elif instru == 'dump':
            rospy.loginfo("Dump: dumping product.")

            # Result false as error because no object in area.
            if not self.ir_end:
                rospy.logerr("Dump: dumping product.")
                result.gelukt = False
                result.bericht = "Geen product gedetecteerd om te dumpen."
                self._as.set_succeeded(result)
                return

            self.motor_pub.publish(Bool(data=True))
            # wait for object to leave the sensor
            while not rospy.is_shutdown() and self.ir_end:
                rate.sleep()
            rospy.loginfo("Product is verdwenen voor de sensor.")

            # Keep spinning for a second and stop
            rospy.sleep(2.0)
            self.motor_pub.publish(Bool(data=False))
            rospy.loginfo("Motor gestopt, dump is succesvol.")

            result.gelukt = True
            result.bericht = "Dump sequence complete"
            self._as.set_succeeded(result)

        else:
            result.gelukt   = False
            result.bericht = "onbekende instructie"
            self._as.set_aborted(result)

if __name__ == '__main__':
    node = TransportController()
    rospy.spin()