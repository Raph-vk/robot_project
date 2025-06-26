#!/usr/bin/env python
# -*- coding: utf-8 -*-
# HMI met Flask + ROS (statusvisualisatie en knopacties)
# Deze HMI ontvangt de status van een ROS-hoofdprogramma en toont die visueel via lampkleuren en tekst.
# Alleen knopcommando's (start, stop, reset, etc.) worden teruggestuurd naar ROS.

from flask import Flask, render_template, request, jsonify
import os
import rospy
from std_msgs.msg import Bool, String
import threading

class HMI:
    def __init__(self):
        # Init Flask
        self.app = Flask(__name__, template_folder=os.path.join(os.path.dirname(__file__), '../templates'))

        # Publishers
        self.start_pub = rospy.Publisher('/start', Bool, queue_size=1, latch=False)
        self.start_continue_pub = rospy.Publisher('/start_continue', Bool, queue_size=1)
        self.stop_pub = rospy.Publisher('/stop', Bool, queue_size=1)
        self.reset_pub = rospy.Publisher('/reset', Bool, queue_size=1)

        # Interne toestand van de HMI
        self.machine_state = "Initialiseren"
        self.lamp_state = ["off"]
        self.orange_blink = False

        # Subscribers
        rospy.Subscriber('/hmi/status', String, self.status_callback)

        # Webroute
        self.app.add_url_rule('/', 'index', self.index, methods=['GET', 'POST'])
        self.app.add_url_rule('/status', 'status', self.status_json)

        self.run()
        rospy.spin()

    def status_callback(self, msg):
        status = msg.data.upper()
        self.orange_blink = False # Reset knipperen bij nieuwe status

        if status == "WACHTEN_OP_START":
            self.machine_state = "WachtOpStart"
            self.lamp_state = ["green"]
        elif status == "IN_BEDRIJF":
            self.machine_state = "In bedrijf"
            self.lamp_state = ["orange"]
        elif status == "FOUT":
            self.machine_state = "Fout opgetreden"
            self.lamp_state = ["green", "orange"]    
            self.orange_blink = True
        elif status == "ERROR":
            self.machine_state = "ERROR, controleer machine"
            self.lamp_state = ["red"]
        elif status == "Initialiseren":
            self.machine_state = "Initialiseren"
            self.lamp_state = ["off"]
        else:
            self.machine_state = "FOUT, Onbekende state"
            self.lamp_state = ["red"]

    def index(self):
        if request.method == 'POST':
            action = request.form.get('action')

            if action == 'start_cycle':
                self.start_pub.publish(True)
            elif action == 'continue_cycle':
                self.start_continue_pub.publish(True)
            elif action == 'stop':
                self.stop_pub.publish(True)
                self.orange_blink = True
            elif action == 'reset':
                self.reset_pub.publish(True)

        return render_template('hmi_gui.html', state=self.machine_state, lamp_state=self.lamp_state)

    def status_json(self):
        return jsonify({
            'state': self.machine_state,
            'lamp_state': self.lamp_state,
            'orange_blink': self.orange_blink
        })

    def run(self):
        thread = threading.Thread(
            target=self.app.run,
            kwargs={'host': '0.0.0.0', 'port': 5000, 'debug': False}
        )
        thread.daemon = True
        thread.start()

if __name__ == '__main__':

    rospy.init_node('hmi_node')
    rospy.loginfo("ROS-node 'hmi_node' is geïnitialiseerd")

    try:
        HMI()
    except rospy.ROSInterruptException:
        pass