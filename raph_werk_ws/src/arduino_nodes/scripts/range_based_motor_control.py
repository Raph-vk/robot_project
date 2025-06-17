#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Range
from std_msgs.msg import Bool

# Threshold below which the motor should turn OFF
SWITCH_DISTANCE = 0.15  # meters
EMPTY_DISTANCE = 1.0 # meters

class RangeBasedMotorControl:
    def __init__(self):
        rospy.init_node('range_based_motor_control')

        # Publisher to control motor
        self.motor_pub = rospy.Publisher('/motor_switch', Bool, queue_size=1)

        # Subscriber to range data
        rospy.Subscriber('/sensor_info', Range, self.range_callback)

        # Keep track of motor state to avoid spamming commands
        self.motor_on = True

        rospy.loginfo("Range-based motor control node started.")
        rospy.spin()

    def range_callback(self, msg):
	# Print the distance
	distance = msg.range
        rospy.loginfo("Distance received: %.2f m", distance)

        # Log the current motor state
        current_motor_state_str = "ON" if self.motor_on else "OFF"
        rospy.loginfo("Current commanded motor state: %s", current_motor_state_str)

        # Decision logic

        # Object is dichtbij de sensor, dus stop de motor
        if distance < SWITCH_DISTANCE and self.motor_on:
            rospy.logwarn("Eindpunt gearriveerd, stop de motor.")
            self.motor_pub.publish(Bool(data=False))
            self.motor_on = False

        # Geen object gezien, dus stop de motor
        elif distance >= EMPTY_DISTANCE and self.motor_on:
            rospy.loginfo("Transportband is leeg, stop de motor.")
            self.motor_pub.publish(Bool(data=False))
            self.motor_on = False

        # Object gezien, start de motor
        elif distance >= SWITCH_DISTANCE and not self.motor_on:
            rospy.loginfo("Object gedetecteerd, start de motor.")
            self.motor_pub.publish(Bool(data=True))
            self.motor_on = True

if __name__ == '__main__':
    try:
        RangeBasedMotorControl()
    except rospy.ROSInterruptException:
        pass

