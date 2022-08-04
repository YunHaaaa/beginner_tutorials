#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

bridge = CvBridge()

def listener():
    rospy.init_node('webcam_sub', anonymous=True)
    rospy.Subscriber("webcam_image", Image, callback)
    rospy.spin()

def callback(data):
    rospy.loginfo("received an image!")
    cv2_img = bridge.imgmsg_to_cv2(data, "bgr8")

if __name__ == '__main__':
    listener()     

