#!/usr/bin/env python3
from copy import deepcopy
from queue import Empty
import rospy
from std_msgs.msg import String
from visualization_msgs.msg import Marker
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
from geometry_msgs.msg import PoseStamped
import tf2_ros
import tf2_geometry_msgs
from moveit_python.geometry import rotate_pose_msg_by_euler_angles, translate_pose_msg
import math
from std_msgs.msg import Empty
from set_niryo_moveit import niryo_moveit
from ar_track_alvar_msgs.msg import AlvarMarkers
from moveit_python.geometry import rotate_pose_msg_by_euler_angles, translate_pose_msg

MARKER_ID = "ar_marker_1"

class Tag_nav():
  '''Class for reacting to aruco_tags.'''

  def __init__(self):
    rospy.init_node('lab_pose', anonymous=True)
    rospy.loginfo("Initialized Lab Pose Node")
    self.move_arm = niryo_moveit("arm")
    self.gripper_open = rospy.Publisher('/gripper/open', Empty, queue_size=1)
    self.gripper_close = rospy.Publisher('/gripper/close', Empty, queue_size=1)
    self.marker_sub = rospy.Subscriber("/ar_pose_marker", AlvarMarkers, self.callback_marker, queue_size=1)
    self.tf_buffer = tf2_ros.Buffer()
    tf_listener = tf2_ros.TransformListener(self.tf_buffer)
    self.grasp_pose_pub = rospy.Publisher("/grasp_pose", PoseStamped, queue_size=1)

    
  def callback_marker(self, data): # data is a PoseStamped object    

    # log and publish
    rospy.loginfo("Marker msg was: \n %s", data)
    
    # ADD YOUR CODE HERE
    
    
    rospy.loginfo("Transformed pose is: \n %s", grasp_pose)
    
    # open gripper
    self.gripper_open.publish()   
    # grasp pose
    self.publish_grasp_pose(grasp_pose)
    # send pose goal to arm
    self.move_arm.move_to(grasp_pose) 
    # close gripper
    self.gripper_close.publish()
    
    # ADD YOUR CODE HERE to MOVE arm somewhere else and drop object

  def publish_grasp_pose(self, grasp_pose):
    self.grasp_pose_pub.publish(grasp_pose)

# If the python node is executed as main process (sourced directly)
if __name__ == '__main__':
  try:
      ar_nav = Tag_nav()
      rospy.spin()
  except rospy.ROSInterruptException:
      rospy.loginfo("Script finished.")  
