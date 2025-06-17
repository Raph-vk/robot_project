#!/usr/bin/env python
'''
Type: Programma
Naam programma: vision_systeem.py

Programmeur 1: Marijn Nieuwenhuize
Programmeurnummer: 2214688

Vak: Robotica in de machinebouw
Locatie: Breda
Datum: 12-6-2025
Versie: 1.1

Functionele beschrijving:
Hoofdfunctie:
Detecteren en publiceren van positie, orientatie en type tandenborstel wanneer /vision service
wordt geactiveerd. 

Deelfuncties:
Initialiseren van Node /vision_systeem_node
Starten vision systeem bij activatie van /vision service
Neural Network Detectie data uitlezen
Positie publiceren
Type tandenborstel publiceren 
Orientatie klasse activeren
Orientatie en positie publiceren als PoseStamped
Mogelijk foutmelding terug sturen naar /vision service
'''

import rospy
from std_msgs.msg import Int32
from depthai_ros_msgs.msg import SpatialDetectionArray
from geometry_msgs.msg import PoseStamped
from std_srvs.srv import SetBool, SetBoolResponse
from tf.transformations import quaternion_from_euler
from orientatie import Bepalen_orientatie
import math

# Globale variabelen
slagingspercentage=0.6

#Pre: /vision service gecalled
#Post: Sturen van True met Succesbericht naar Service
#Post: Sturen van False met Foutmelding naar Service
def start_vision(request):
    try:
        #Voer eenmalig vision uit
        msg = rospy.wait_for_message('/stereo_inertial_nn_publisher/color/detections', SpatialDetectionArray, timeout=5.0)
        detecteer_en_publiceer(msg)
        return SetBoolResponse(success=True, message="Detectie en publicatie gelukt")
    except Exception as e:
        rospy.logerr("Fout tijdens vision service: %s" % str(e))
        return SetBoolResponse(success=False, message="Fout: %s" % str(e))

#Pre: Detectie data van Neural Network
#Post: Type tandenborstel wordt als getal gestuurd naar /type_tb topic
#Post: Positie en orientatie wordt als PoseStamped gestuurd naar /pos_tb_camera topic
def detecteer_en_publiceer(msg): 
     if not msg.detections:
        raise ValueError("Geen objecten gedetecteerd")
     
     #Vind de meest linksboven gedetecteerde object
     linksboven_detectie = min(msg.detections,key=lambda d: (d.bbox.center.x, d.bbox.center.y))
     
     #Bepaal of percentage nauwkeurigheid van detectie hoger is als slagingspercentage
     percentage= linksboven_detectie.results[0].score
     if percentage<slagingspercentage:
        raise ValueError("Object is niet nauwkeurig gedetecteerd")
     
     #Bepaal klasse id en positie van de meest linksboven gedetecteerde object
     klasse_id = linksboven_detectie.results[0].id
     positie = linksboven_detectie.position
     
     # Maak PoseStamped object aan
     pose_msg = PoseStamped()
     pose_msg.header.stamp = rospy.Time.now()
     pose_msg.header.frame_id = "oak_rgb_camera_optical_frame"  
     pose_msg.pose.position = positie
     
     #Bepalen hoek rond x-as
     Bepaler=Bepalen_orientatie(linksboven_detectie)
     #Wacht even zodat orientatie bepaald kan worden
     hoek_deg=Bepaler.get_hoek()
     #Als hoek 1000 is bepalen van orientatie gefaald
     if hoek_deg==1000:
         raise ValueError("Kon hoek niet vinden")
     
     rospy.loginfo(hoek_deg)
     hoek_rad=math.radians(hoek_deg)
     #Toevoeg orientatie aan PostStamped object
     q = quaternion_from_euler(0, 0, hoek_rad)
     pose_msg.pose.orientation.x = q[0]
     pose_msg.pose.orientation.y = q[1]
     pose_msg.pose.orientation.z = q[2]
     pose_msg.pose.orientation.w = q[3]
     
     #Publiceer Posestamp en type tandenborstel
     pubPositie.publish(pose_msg)
     pubKlasse.publish(klasse_id)	 

if __name__ == '__main__':
    global pubPositie, pubKlasse
   
    #Intializeer node
    rospy.init_node('vision_systeem_node')
    rospy.loginfo("Vision Gestart")
   
    # Publishers
    pubPositie = rospy.Publisher('/pos_tb_camera', PoseStamped, queue_size=1)
    pubKlasse = rospy.Publisher('/type_tb', Int32, queue_size=1)
    #Services
    start_service=rospy.Service('/vision', SetBool, start_vision)

    rospy.spin()
