#!/usr/bin/env python
# -*- coding: utf-8 -*-
# HMI met Flask + ROS (statusvisualisatie en knopacties)

from flask import Flask, render_template, request
import os
import rospy
from std_msgs.msg import Bool, String
import threading
import time

app = Flask(__name__, template_folder=os.path.join(os.path.dirname(__file__), '../templates'))

rospy.init_node('hmi_node', anonymous=True)
print("[DEBUG] ROS-node 'hmi_node' is geïnitialiseerd")

# ROS publishers
start_pub = rospy.Publisher('/start', Bool, queue_size=1)
start_continue_pub = rospy.Publisher('/start_continue', Bool, queue_size=1)
stop_pub = rospy.Publisher('/stop', Bool, queue_size=1)
reset_pub = rospy.Publisher('/reset', Bool, queue_size=1)
emergency_pub = rospy.Publisher('/emergency_stop', Bool, queue_size=1)

led_rood_pub   = rospy.Publisher('/led_rood', Bool, queue_size=1)
led_oranje_pub = rospy.Publisher('/led_oranje', Bool, queue_size=1)
led_groen_pub  = rospy.Publisher('/led_groen', Bool, queue_size=1)

# Interne status
machine_state   = "WachtOpStart"
lamp_state      = "green"
reset_required  = False
in_cyclus       = False
continue_mode   = False
knipper_stop_event = threading.Event()

def knipper_oranje_lamp():
    while not knipper_stop_event.is_set():
        led_oranje_pub.publish(True)
        time.sleep(0.5)
        led_oranje_pub.publish(False)
        time.sleep(0.5)

def status_callback(msg):
    global machine_state, lamp_state, reset_required, in_cyclus, continue_mode
    status = msg.data.upper()
    print("[DEBUG] Ontvangen status: {}".format(status))
    knipper_stop_event.set()

    if status == "WACHTEN_OP_START":
        machine_state = "WachtOpStart"
        lamp_state = "green"
        reset_required = in_cyclus = continue_mode = False
        led_rood_pub.publish(False)
        led_oranje_pub.publish(False)
        led_groen_pub.publish(True)

    elif status == "IN_BEDRIJF":
        machine_state = "Continue cyclus actief"
        lamp_state = "orange"
        continue_mode = True
        led_rood_pub.publish(False)
        led_groen_pub.publish(False)
        led_oranje_pub.publish(True)

    elif status == "ERROR":
        machine_state = "Fout opgetreden"
        lamp_state = "red"
        reset_required = True
        continue_mode = False
        in_cyclus = False
        led_rood_pub.publish(True)
        led_oranje_pub.publish(False)
        led_groen_pub.publish(False)

    elif status == "STILGESTELD":
        machine_state = "Cyclus gepauzeerd"
        lamp_state = "orange"
        led_rood_pub.publish(False)
        led_groen_pub.publish(False)
        knipper_stop_event.clear()
        threading.Thread(target=knipper_oranje_lamp).start()

rospy.Subscriber('/hmi/status', String, status_callback)
print("[DEBUG] Subscribed op /hmi/status")

@app.route('/', methods=['GET', 'POST'])
def index():
    global machine_state, lamp_state, reset_required, in_cyclus, continue_mode

    if request.method == 'POST':
        action = request.form.get('action')

        if action == 'emergency_stop':
            machine_state = "Noodstop geactiveerd"
            lamp_state = "red"
            reset_required = True
            in_cyclus = continue_mode = False
            emergency_pub.publish(True)
            led_rood_pub.publish(True)
            knipper_stop_event.set()

        elif action == 'stop' and continue_mode:
            machine_state = "Cyclus wordt gestopt"
            lamp_state = "orange"
            stop_pub.publish(True)
            knipper_stop_event.clear()
            threading.Thread(target=knipper_oranje_lamp).start()
            continue_mode = in_cyclus = False

        elif action == 'reset' and reset_required:
            machine_state = "WachtOpStart"
            lamp_state = "green"
            reset_required = False
            led_rood_pub.publish(False)
            led_oranje_pub.publish(False)
            led_groen_pub.publish(True)
            reset_pub.publish(True)
            knipper_stop_event.set()

        elif action == 'start_cycle' and not in_cyclus and not continue_mode and not reset_required:
            machine_state = "Enkele cyclus actief"
            lamp_state = "orange"
            in_cyclus = True
            start_pub.publish(True)
            led_oranje_pub.publish(True)

            def cyclus_afronden():
                time.sleep(5)
                global in_cyclus, machine_state, lamp_state
                in_cyclus = False
                machine_state = "WachtOpStart"
                lamp_state = "green"
                led_oranje_pub.publish(False)
                led_groen_pub.publish(True)

            threading.Thread(target=cyclus_afronden).start()

        elif action == 'continue_cycle' and not in_cyclus and not continue_mode and not reset_required:
            machine_state = "Continue cyclus actief"
            lamp_state = "orange"
            continue_mode = True
            start_continue_pub.publish(True)
            led_oranje_pub.publish(True)

    return render_template('hmi_gui.html', state=machine_state, lamp_state=lamp_state)

if __name__ == '__main__':
    app.run(debug=True)

