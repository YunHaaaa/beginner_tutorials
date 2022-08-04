#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

cap=cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cap.set(cv2.CAP_PROP_FPS, 30)

rospy.init_node("webcam_pub", anonymous=True)
image_pub=rospy.Publisher("webcam_image", Image, queue_size=1)

bridge = CvBridge()

while not rospy.is_shutdown():
    ret, cv_image = cap.read()
    image_pub.publish(bridge.cv2_to_imgmsg(cv_image, "bgr8"))
    cv2.imshow('image', cv_image)
    cv2.waitKey(3)

cap.release()
cv2.destroyAllWindows()
