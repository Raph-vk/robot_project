#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy                                      # ROS Python client library
import actionlib
from std_msgs.msg import Bool                     # For publishing motor on/off
from transportsysteem_pkg.msg import TransportControlAction, TransportControlFeedback, SystemControlResult

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
        feedback = TransportControlFeedback()
        result   = TransportControlResult()
        instru = req.instruction.strip().lower()
        rate = rospy.Rate(10)

        if instru == 'start':            
            rospy.loginfo("Start sequence initiated")
            rospy.loginfo("Looking for object...")
            feedback.feedback = "Looking for object at start"
            self._as.publish_feedback(feedback)

            # wait for object at beginning
            while not rospy.is_shutdown() and not self.ir_begin:
                if self._as.is_preempt_requested():
                    return self._as.set_preempted()
                rate.sleep()

            feedback.feedback = "Object detected, running motor"
            self._as.publish_feedback(feedback)
            self.motor_pub.publish(Bool(data=True))

            # wait for object at end, but give up after 10s
            start_time = rospy.Time.now()
            while not rospy.is_shutdown() and not self.ir_end:
                if self._as.is_preempt_requested():
                    return self._as.set_preempted()

                # timeout check
                if (rospy.Time.now() - start_time).to_sec() > 10.0:
                    rospy.logwarn("Timeout: object did not reach end within 10s")
                    self.motor_pub.publish(Bool(data=False))
                    result.result = False
                    self._as.publish_feedback(
                        SystemControlFeedback(feedback="No object getting to the end"))
                    return self._as.set_succeeded(result)
                rate.sleep()

            rospy.sleep(1.5)
            self.motor_pub.publish(Bool(data=False))
            feedback.feedback = "Reached end, stopping motor"
            self._as.publish_feedback(feedback)


            result.result = True
            self._as.publish_feedback(   # send one last feedback
                SystemControlFeedback(feedback="Start sequence complete"))
            self._as.set_succeeded(result)

        elif instru == 'dump':
            feedback.feedback = "Dump: dumping product."
            self._as.publish_feedback(feedback)

            # Result false as error because no object in area.
            if not self.ir_end:
                result.result = False
                self._as.publish_feedback(   # send one last feedback
                    SystemControlFeedback(feedback="No object in area"))
                self._as.set_succeeded(result)
                return

            self.motor_pub.publish(Bool(data=True))
            # wait for object to leave the sensor
            while not rospy.is_shutdown() and self.ir_end:
                rate.sleep()
    
            # Keep spinning for a second and stop
            rospy.sleep(1.0)
            self.motor_pub.publish(Bool(data=False))

            result.result = True
            self._as.publish_feedback(   # send one last feedback
                SystemControlFeedback(feedback="Dump sequence complete"))
            self._as.set_succeeded(result)

        else:
            result.result   = False
            feedback.feedback = "Unknown instruction"

            self._as.publish_feedback(feedback)
            self._as.set_aborted(result)

if __name__ == '__main__':
    node = TransportController()
    rospy.spin()