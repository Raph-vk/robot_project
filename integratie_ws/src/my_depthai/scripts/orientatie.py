#!/usr/bin/env python
'''
Type: Klase difinitie
Naam programma: orientatie.py

Programmeur 1: Marijn Nieuwenhuize
Programmeurnummer: 2214688

Vak: Robotica in de machinebouw
Locatie: Breda
Datum: 12-6-2025
Versie: 1.2

Functionele beschrijving:
Hoofdfunctie:
Het defineren van klasse voor het bepalen van de orientatie van een tandenborstel met OpenCV functies.

'''
import rospy
import cv2
import numpy as np
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

class Bepalen_orientatie:
     def __init__(self,detection):
          self.bridge = CvBridge()
          self.hoek=1000
          self.detectie = detection
          self.msg =rospy.wait_for_message("/stereo_inertial_nn_publisher/color/image", Image, timeout=5.0 )
          self.image_callback(self.msg)

     #Pre: Kleurenbeeld van Camera A wordt meegeven
     #Post: Hoek van gedetecteerd object wordt bepaald
     #Post: Hoek van gedetecteerd object wordt niet bepaald en hoek blijft 1000     
     def image_callback(self,data):
         
            #Omzetten image naar mat datatype
            img = self.bridge.imgmsg_to_cv2(data, "bgr8")
            h, w = img.shape[:2]
            #Afbeelding besnijden tot enkel zwarte vlak van de Transportband
            x1, y1 = 0,300 
            x2, y2 = 760, 580
            x1, y1 = max(0, x1), max(0, y1)
            x2, y2 = min(w, x2), min(h, y2)
            cropped = img[y1:y2, x1:x2]
            
            #Besnijden afbeelding binair maken met global thresholding
            gray = cv2.cvtColor(cropped, cv2.COLOR_BGR2GRAY)
            _, binair = cv2.threshold(gray, 60, 255, cv2.THRESH_BINARY )
            _, contours, hierarchy = cv2.findContours(binair, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
            bbox=self.detectie.bbox
            
            #Contours filteren op area
            min_area = 1000 
            contours = [c for c in contours if cv2.contourArea(c) > min_area]
            max_area = 10000000 
            contours = [c for c in contours if cv2.contourArea(c) < max_area]

            #Postie centrum van bounding box van gedetecteerde object wordt omgezet naar juiste 
            #positie in besnijden afbeelding
            center_point = (bbox.center.x - x1, bbox.center.y - y1)

            #Ga langs alle contours en bepaal minimale rechthoek rond voor elke contour
            #Controleer of deze rechthoek het centrum van bounding box van gedetecteerde object bevat
            #Bepaal hoek met deze rechthoek als centrum in rechthoek zit
            for contour in contours:
             rect = cv2.minAreaRect(contour)
             box = cv2.boxPoints(rect)
             contour = np.array(box, dtype=np.int32).reshape((-1,1,2))
             result = cv2.pointPolygonTest(contour, center_point, False)
             if result >= 0:
                  _, (width, height), angle = rect
                  if width < height:
                     angle += 90
                  self.hoek=angle 

     def get_hoek(self):
         return self.hoek


