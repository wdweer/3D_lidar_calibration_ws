#!/usr/bin/env/python3
# -*- coding: utf-8 -*-
import rospy
import tf
from geometry_msgs.msg import PoseStamped


if __name__ == '__main__':
    rospy.init_node("tf_listener")

    tf_listener = tf.TransformListener()    # TF Listener 객체 선언

    r = rospy.Rate(1)
    while not rospy.is_shutdown():

        if tf_listener.canTransform(
                target_frame="base_link", source_frame="hokuyo_laser_link", time=rospy.Time(0)):
            tf_matrix = tf_listener.lookupTransform(
                target_frame="base_link", source_frame="hokuyo_laser_link1", time=rospy.Time(0))

            rospy.loginfo(tf_matrix)

        else:
            rospy.logwarn("Cannot lookup transform between world and home")

        r.sleep()