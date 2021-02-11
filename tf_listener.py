#!/usr/bin/env python

from __future__ import print_function

import rospy
import tf
import geometry_msgs.msg

if __name__ == '__main__':
    rospy.init_node('tf_listener')

    listener = tf.TransformListener()
    br = tf.TransformBroadcaster()

    rate = rospy.Rate(10.0)
    while not rospy.is_shutdown():
        try:
            (trans,rot) = listener.lookupTransform('/world_frame', '/item', rospy.Time(0))
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            continue
        print ('[x y z] = ', trans)
        print ('[r p y] = ', tf.transformations.euler_from_quaternion(rot))

        rate.sleep()




