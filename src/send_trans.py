#!/usr/bin/env python  
import roslib
import rospy
import tf
 
if __name__ == '__main__':
    rospy.init_node('my_tf_broadcaster')
    br = tf.TransformBroadcaster()
    rate = rospy.Rate(10.0) # 10 hz
    print("Sending transform...")
    while not rospy.is_shutdown():
         # sendTransform(translation, rotation, time, child, parent)
        br.sendTransform((1.0, 0.0, 0.0),
                          (0.0, 0.0, 0.0, 1.0),
                          rospy.Time.now(),
                          "item",
                          "summit_xl_front_rgbd_camera_depth_optical_frame")
        br.sendTransform((0.0, 0.0, 0.0),
                          (0.0, 0.0, 0.0, 1.0),
                          rospy.Time.now(),
                          "summit_xl_odom",
                          "world_frame")

         # print("Sent tf transform")
        rate.sleep()
         # print("Time should have passed")



