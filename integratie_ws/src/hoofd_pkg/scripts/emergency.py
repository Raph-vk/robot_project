#!/usr/bin/env python
'''
Type: Programma
Naam programma: emergency.py

Programmeur 1: Marijn Nieuwenhuize
Programmeurnummer: 2214688

Vak: Robotica in de machinebouw
Locatie: Breda
Datum: 19-6-2025
Versie: 0.1

Functionele beschrijving:
Hoofdfunctie:


Deelfuncties:

'''
import rospy
import os
import actionlib
from actionlib_msgs.msg import GoalID
from actionlib_msgs.msg import GoalStatusArray
from std_msgs.msg import Bool
from xarm_msgs.srv import GetErr
from robotarm.msg import manipulatorAction, manipulatorFeedback, manipulatorResult
from transportsysteem_pkg.msg import TransportControlAction, TransportControlFeedback, SystemControlResult


cancel_status = {}
timeout_Cancelen = rospy.Duration(2)
timeout_Killen = rospy.Duration(60)

def status_callback(msg, action_name):
    if not msg.status_list:
        cancel_status[action_name] = False
    latest_status = msg.status_list[-1].status
    if latest_status in [2, 3, 4, 5, 8]:  
        cancel_status[action_name] = True
    else:
        cancel_status[action_name] = False

def cancel_actions():
    actions = [
        '/manipulator_action',
        '/transport_control',
    ]

    for action in actions:
        #Zet status van actions als niet gecanceld
        cancel_status[action] = False  

        rospy.Subscriber(action + "/status", GoalStatusArray, status_callback, callback_args=action)

        # Vraag aan action om te cancelen
        topic = action + "/cancel"
        pub = rospy.Publisher(topic, GoalID, queue_size=1, latch=True)
        start_time = rospy.Time.now()
        # Controleer of er binnen 2 seconden de action verbonden is met publisher
        while pub.get_num_connections() == 0:
            if rospy.Time.now() - start_time > timeout_Cancelen:
                rospy.logerr("Timeout: Kon niet verbinden met %s", topic)
                kill_node(action)
                break
            rospy.sleep(0.1)
        pub.publish(GoalID())
        rospy.loginfo("Cancel aangevraagt naar %s", topic)

        #Controleer of er binnen 2 seconden de action geschikt is om opnieuw een goal te ontvangen
        start_time = rospy.Time.now()
        while not cancel_status[action]:
            if rospy.Time.now() - start_time > timeout_Cancelen:
                rospy.logerr("Timeout: Kon action niet cancellen %s", action)
                kill_node(action)
                break
            rospy.sleep(0.1)

    rospy.loginfo("All action goals zijn gecanceled of gerelaunched.")
def kill_node(action):
     if action=="/transport_control":
         rospy.loginfo("Killen en relaunchen van transportband programma")
         
         os.system("rosnode kill /transport_control_node /arduino_node")
         os.system("roslaunch transportsysteem_pkg transport_control.launch &")
         rospy.sleep(2)
         client = actionlib.SimpleActionClient(action,TransportControlAction)
         if not client.wait_for_server(timeout_Killen):
             rospy.logfatal("Killen en relaunchen van transportband programma mislukt")
             rospy.logfatal("Systeem kan terminator niet herstarten")
             rospy.logfatal("Systeem wordt afgesloten") 
             kill_alle_ros_nodes()
          
     if action=="/manipulator_action":
         rospy.loginfo("Killen en relaunchen van manipulator programma")
         os.system("rosnode kill /manipulator_node")
         os.system("roslaunch robotarm robotcel.launch &")
         rospy.sleep(2)
         client = actionlib.SimpleActionClient(action, manipulatorAction)
         if not client.wait_for_server(timeout_Killen):
             rospy.logfatal("Killen en relaunchen van manipulator programma mislukt")
             rospy.logfatal("Systeem kan terminator niet herstarten")
             rospy.logfatal("Systeem wordt afgesloten") 
             kill_alle_ros_nodes()

def kill_alle_ros_nodes():
    os.system("rosnode kill -a")
    os.system("pkill -f roslaunch")
    os.system("pkill -f rosout")
    os.system("pkill -f rosmaster")


def poll_errors():
    rospy.wait_for_service('/ufactory/get_err')
    get_err = rospy.ServiceProxy('/ufactory/get_err', GetErr)

    rate = rospy.Rate(2)  # check 2 times per second
    while not rospy.is_shutdown():
        try:
            response = get_err()
            if response.err == 2:
                rospy.logwarn("❗ Error C2 gedetecteerd — Noodstop wordt geactiveerd!")
                pub_nood.publish(True)
                cancel_actions()
                pub_succes.publish(True)
        except rospy.ServiceException as e:
            rospy.logerr("GetErr service call is gefailed: %s", str(e))
            kill_node("/transport_control")
            kill_node("/manipulator_action")
        rate.sleep()

if __name__ == '__main__':
    #Intializeer node
    rospy.init_node("emergency_node")
    rospy.loginfo("Noodstop systeem gestart")

    #Publisher
    pub_nood=rospy.Publisher("/Noodstop_aan",Bool, queue_size=1)
    pub_succes=rospy.Publisher("/Noodstop_afgehandeld",Bool, queue_size=1)
   
    #Services
    poll_errors()
