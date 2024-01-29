#! /usr/bin/env python3

"""
2D Lidar Subscriber example

referenced from wiki.ros.org

url: http://wiki.ros.org/ROS/Tutorials/WritingPublisherSubscriber%28python%29
"""

import rospy
from sensor_msgs.msg import LaserScan
import numpy as np

class Trans():
    def __init__(self):
        self.sub = rospy.Subscriber("/hokuyo/hokuyo_tf/laser_scan", LaserScan, self.lidar_callback)
    def lidar_callback(self, data):
        self.lidar_data=data.ranges
        self.lidar_matrix=[self.lidar_data]
        self.lidar_matrix=np.array(self.lidar_matrix).reshape(80,4)
        print(self.lidar_matrix)
        
        
    


rospy.loginfo(
    "==== Laser Scan Subscriber node Started, move forward during 10 seconds ====\n"
)

rospy.init_node("laser_scan")
while not rospy.is_shutdown():
    start=Trans()
    r=rospy.Rate(10)
    r.sleep()