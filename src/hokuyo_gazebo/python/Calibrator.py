#!/usr/bin/env python

import rospy 
from sensor_msgs.msg import LaserScan
import numpy as np
from sensor_msgs.msg import PointCloud2
from geometry_msgs.msg import TransformStamped
class Trans():
    def __init__(self):
        rospy.init_node('Calibrator')
        self.sub1 = rospy.Subscriber("/hokuyo/hokuyo_tf/laser_scan", LaserScan, self.lidar_callback1)
        self.sub2 = rospy.Subscriber("/hokuyo/hokuyo/laser_scan", LaserScan, self.lidar_callback2)
        self.sub3 = rospy.Subscriber("/ambient_pointcloud", PointCloud2, self.cali_callback)
        self.pub1 = rospy.Publisher("/laser_scan", LaserScan, queue_size=1)
        self.pub2 = rospy.Publisher("/laser_scan", LaserScan, queue_size=1)
    def lidar_callback1(self, data):
        self.lidar_data1=data.ranges
        self.lidar_matrix1=[self.lidar_data1]
        self.lidar_matrix1=np.array(self.lidar_matrix1).reshape(80,4)
        self.pub1.publish(data)
        
    def lidar_callback2(self, data):
        self.lidar_data2=data.ranges
        self.lidar_matrix2=[self.lidar_data2]
        self.lidar_matrix2=np.array(self.lidar_matrix2).reshape(80,4)
        self.pub2.publish(data)
        self.t1 = TransformStamped()

    def cali_callback(self,data):
        print(data)
while not rospy.is_shutdown():
    start=Trans()
    r=rospy.Rate(10)
    r.sleep()


