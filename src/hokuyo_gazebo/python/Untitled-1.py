#!/usr/bin/env python

import rospy 
from sensor_msgs.msg import LaserScan
import numpy as np


class Trans():
    def __init__(self):
        rospy.init_node('Calibrator')
        self.sub1 = rospy.Subscriber("/hokuyo/hokuyo_tf/laser_scan", LaserScan, self.lidar_callback1)
        self.sub2 = rospy.Subscriber("/hokuyo/hokuyo/laser_scan", LaserScan, self.lidar_callback2)
        self.pub1 = rospy.Publsiher("/lidar_0/lidar_node/pointcloud", LaserScan, queue_size=1)
        self.pub2 = rospy.Publsiher("/lidar_1/lidar_node/pointcloud", LaserScan, queue_size=1)
    def lidar_callback1(self, data):
        self.lidar_data1=data.ranges
        self.lidar_matrix1=[self.lidar_data1]
        self.lidar_matrix1=np.array(self.lidar_matrix1).reshape(80,4)
        self.pub1.publish(self.lidar_matrix1)
    def lidar_callback2(self, data):
        self.lidar_data2=data.ranges
        self.lidar_matrix2=[self.lidar_data2]
        self.lidar_matrix2=np.array(self.lidar_matrix2).reshape(80,4)
        self.pub2.publish(self.lidar_matrix2)




rospy.spin()