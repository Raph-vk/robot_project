#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Point, PoseStamped, Quaternion
from std_msgs.msg import Int32

if __name__ == '__main__':
    rospy.init_node('vision_node')

    pubPositie = rospy.Publisher('/pos_tb_camera', PoseStamped, queue_size=1)
    pubKlasse = rospy.Publisher('/type_tb', Int32, queue_size=1)

    rospy.sleep(0.5)
    
    locatie_object = PoseStamped()
    locatie_object.header.frame_id = "oak_d_rgb_camera_optical_frame"  
    locatie_object.pose.position = Point(x=-0.01, y=0.002, z=0.45)
    locatie_object.pose.orientation = Quaternion(x=0, y=0, z=-0.382683432365, w=0.923879532511)

    type_object = Int32()
    type_object.data = 4  # 0=blauw 1=geel 3=wit 4=paars
    
    pubPositie.publish(locatie_object)
    pubKlasse.publish(type_object)

    rospy.sleep(5)  # of langer





