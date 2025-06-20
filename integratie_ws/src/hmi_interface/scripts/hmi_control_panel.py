#!/usr/bin/env python
# -*- coding: utf-8 -*-
# HMI met Flask + ROS (statusvisualisatie en knopacties)
# Deze HMI ontvangt de status van een ROS-hoofdprogramma en toont die visueel via lampkleuren en tekst.
# Alleen knopcommando's (start, stop, reset, etc.) worden teruggestuurd naar ROS.

from flask import Flask, render_template, request
import os
import rospy
from std_msgs.msg import Bool, String
import threading

# Initialiseer Flask-applicatie (webserver voor de HMI)
app = Flask(__name__, template_folder=os.path.join(os.path.dirname(__file__), '../templates'))

# Initialiseer ROS-node
rospy.init_node('hmi_node', anonymous=True)
print("[DEBUG] ROS-node 'hmi_node' is geïnitialiseerd")

# ROS publishers voor bedieningsknoppen (HMI → Hoofdprogramma)
start_pub = rospy.Publisher('/start', Bool, queue_size=10)
start_continue_pub = rospy.Publisher('/start_continue', Bool, queue_size=10)
stop_pub = rospy.Publisher('/stop', Bool, queue_size=10)
reset_pub = rospy.Publisher('/reset', Bool, queue_size=10)
emergency_pub = rospy.Publisher('/emergency_stop', Bool, queue_size=10)

# Interne toestand van de HMI
machine_state = "WachtOpStart"   # statuslabel voor de gebruiker
lamp_state = "green"             # kleur voor de visuele lamp
reset_required = False           # reset-knop alleen actief na fout
in_cyclus = False                # true tijdens een enkele cyclus
continue_mode = False            # true tijdens een continue cyclus

# Variabelen om LED-status bij te houden op basis van ROS-subscriptions
_led_red = False
_led_orange = False
_led_green = False
_led_lock = threading.Lock()  # zorgt voor thread-safe updates

# Bepaalt lampkleur aan de hand van de drie ROS-LED-booleans
# Deze functie wordt aangeroepen bij elke LED-wijziging

def _update_lamp_state():
    global lamp_state
    with _led_lock:
        if _led_red:
            lamp_state = "red"
        elif _led_green:
            lamp_state = "green"
        elif _led_orange:
            lamp_state = "orange"
        else:
            lamp_state = "off"

# Callbackfuncties voor LED-topics uit het hoofdprogramma

def led_rood_callback(msg):
    global _led_red
    _led_red = msg.data
    _update_lamp_state()

def led_oranje_callback(msg):
    global _led_orange
    _led_orange = msg.data
    _update_lamp_state()

def led_groen_callback(msg):
    global _led_green
    _led_green = msg.data
    _update_lamp_state()

# ROS-subscriptions voor de LED-status
rospy.Subscriber('/led_rood', Bool, led_rood_callback)
rospy.Subscriber('/led_oranje', Bool, led_oranje_callback)
rospy.Subscriber('/led_groen', Bool, led_groen_callback)

# Callback voor de globale machinestatus, afkomstig van het hoofdprogramma
# Dit beïnvloedt o.a. of reset mogelijk is en wat de gebruiker in beeld ziet

def status_callback(msg):
    global machine_state, reset_required, in_cyclus, continue_mode
    status = msg.data.upper()
    print("[DEBUG] Ontvangen status: {}".format(status))

    if status == "WACHTEN_OP_START":
        machine_state = "WachtOpStart"
        reset_required = in_cyclus = continue_mode = False

    elif status == "IN_BEDRIJF":
        machine_state = "Continue cyclus actief"
        continue_mode = True
        in_cyclus = False

    elif status == "ERROR":
        machine_state = "Fout opgetreden"
        reset_required = True
        continue_mode = in_cyclus = False

    elif status == "STILGESTELD":
        machine_state = "Cyclus gepauzeerd"

# ROS-subscription op de globale machinestatus
rospy.Subscriber('/hmi/status', String, status_callback)
print("[DEBUG] Subscribed op /hmi/status en LED-topics")

# Webroute voor de hoofdpagina van de HMI
@app.route('/', methods=['GET', 'POST'])
def index():
    global machine_state, reset_required, in_cyclus, continue_mode

    # Als een knop wordt ingedrukt
    if request.method == 'POST':
        action = request.form.get('action')

        # Noodstop activeert foutstatus
        if action == 'emergency_stop':
            machine_state = "Noodstop geactiveerd"
            reset_required = True
            in_cyclus = continue_mode = False
            emergency_pub.publish(True)

        # Stopknop onderbreekt continue modus
        elif action == 'stop' and continue_mode:
            machine_state = "Cyclus wordt gestopt"
            stop_pub.publish(True)
            continue_mode = in_cyclus = False

        # Reset alleen mogelijk als foutstatus actief is
        elif action == 'reset' and reset_required:
            machine_state = "WachtOpStart"
            reset_required = False
            reset_pub.publish(True)

        # Enkele cyclus starten als machine idle is
        elif action == 'start_cycle' and not in_cyclus and not continue_mode and not reset_required:
            machine_state = "Enkele cyclus actief"
            in_cyclus = True
            start_pub.publish(True)

        # Continue cyclus starten als machine idle is
        elif action == 'continue_cycle' and not in_cyclus and not continue_mode and not reset_required:
            machine_state = "Continue cyclus actief"
            continue_mode = True
            start_continue_pub.publish(True)

    # Toon de HTML-template met huidige status en lampkleur
    return render_template('hmi_gui.html', state=machine_state, lamp_state=lamp_state)

# Start de Flask webserver
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

