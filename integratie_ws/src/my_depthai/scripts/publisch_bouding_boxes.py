#!/usr/bin/env python
'''
	circle_detector.py
	Purpose: displays boxes around detected objects
	@author Gerard Harkema
	@version 0.9 2023/01/05
    License: CC BY-NC-SA
'''

from __future__ import print_function

import roslib
import sys
import rospy
import cv2
import numpy as np
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import sensor_msgs.point_cloud2 as pc2
from depthai_ros_msgs.msg import SpatialDetectionArray
import random
import json



class detection_displayer:

    def __init__(self, config_file):
        rospy.loginfo(config_file)
        self.display_image = False


        self.colors = []
        colors = []
        with open(config_file, 'r') as f:
            self.model_objects = json.loads(f.read())
            try:
                self.class_names = self.model_objects["class_names"]
                colors = self.model_objects["colors"]
                for color in colors:
                    self.colors.append(colors[color])
            except:
                self.class_names = self.model_objects["mappings"]["labels"]
                for class_name in self.class_names:
                    self.colors.append("#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)]))

        #rospy.loginfo(self.class_names)
        #rospy.loginfo(self.colors)


        self.image_pub = rospy.Publisher("/image_out", Image, queue_size = 10)

        self.bridge = CvBridge()
        self.image_sub = rospy.Subscriber("/image_in", Image, self.image_callback)

        self.detections_sub = rospy.Subscriber("/detections", SpatialDetectionArray, self.detections_callback)

        self.image_received = False

    def detections_callback(self, detections_data):

        if self.image_received:
            for detection in detections_data.detections:
                x1 = detection.bbox.center.x - (detection.bbox.size_x / 2)
                y1 = detection.bbox.center.y - (detection.bbox.size_y / 2)
                x2 = detection.bbox.center.x + (detection.bbox.size_x / 2)
                y2 = detection.bbox.center.y + (detection.bbox.size_y / 2)
                #spatial detections
                x = detection.position.x
                y = detection.position.y
                z = detection.position.z


                class_index = detection.results[0].id
                class_color = self.colors[int(class_index)].strip("#")
                class_color = tuple(int(class_color[i:i + 2], 16) for i in (0, 2, 4))

                cv2.rectangle(self.image, (int(x1), int(y1)), (int(x2), int(y2)), class_color, 2)

                text = '%s: %.2f%%' % (self.class_names[detection.results[0].id], detection.results[0].score * 100)
                #print(text)
                image = cv2.putText(self.image, text, (int(x1)+5, int(y2)-5), cv2.FONT_HERSHEY_SIMPLEX, 1, class_color, 2, cv2.LINE_AA)
                text = 'x: %.3f m' % (x)
                image = cv2.putText(self.image, text, (int(x1)+5, int(y2)+20), cv2.FONT_HERSHEY_SIMPLEX, 1, class_color, 2, cv2.LINE_AA)
                text = 'y: %.3f m' % (y)
                image = cv2.putText(self.image, text, (int(x1)+5, int(y2)+45), cv2.FONT_HERSHEY_SIMPLEX, 1, class_color, 2, cv2.LINE_AA)
                text = 'z: %.3f m' % (z)
                image = cv2.putText(self.image, text, (int(x1)+5, int(y2)+70), cv2.FONT_HERSHEY_SIMPLEX, 1, class_color, 2, cv2.LINE_AA)

            try:
                #if(self.image):
                self.image_pub.publish(self.bridge.cv2_to_imgmsg(self.image, "bgr8"))
                #self.image = None
            except CvBridgeError as e:
                print(e)
            self.image_received = False

    def image_callback(self,data):
        #rospy.loginfo("image Callback")
        try:
            self.image = self.bridge.imgmsg_to_cv2(data, "bgr8")
            #self.image = cv_image.copy()
        except CvBridgeError as e:
            print(e)

        self.image_received = True

        if self.display_image:
            cv2.imshow("Detections window", cv_image)
            cv2.waitKey(3)


def main(args):

    rospy.init_node('publisch_bouding_boxes', anonymous=True)

    node_name = rospy.get_name()

    nnConfig = rospy.get_param(node_name + '/nnConfig') # node_name/argsname
    resourceBaseFolder = rospy.get_param(node_name + '/resourceBaseFolder') # node_name/argsname

    ic = detection_displayer(resourceBaseFolder + '/'+ nnConfig)
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("Shutting down")
        #cv2.destroyAllWindows()

if __name__ == '__main__':
    main(sys.argv)
