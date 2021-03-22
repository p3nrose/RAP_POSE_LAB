#!/usr/bin/env python
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
from std_msgs.msg import Float64
from set_niryo_moveit import niryo_moveit


class Tag_nav():
  '''Class for reacting to aruco_tags.'''

  def __init__(self):
    rospy.init_node('lab5_nav', anonymous=True)
    rospy.loginfo("Initialized Lab5 Node")
    self.move_arm = niryo_moveit("arm")
    self.gripper_pub1 = rospy.Publisher('/gripper_left_controller/command', Float64, queue_size=1)
    self.gripper_pub2 = rospy.Publisher('/gripper_right_controller/command', Float64, queue_size=1)

    # ADD YOUR CODE HERE

    
  def callback_marker(self,data):

        # ADD YOUR CODE HERE


  def publish_camera_pose_from_marker(self, pose_tag, tag_id):

        # ADD YOUR CODE HERE

  def publish_grasp_pose(self, tag, tag_id):
    
        # ADD YOUR CODE HERE

  def gripper_client(self, value):
    rospy.sleep(0.5)
    self.gripper_pub1.publish(-value)
    self.gripper_pub2.publish(value)

  def callback_grasp(self,data):
 
     # ADD YOUR CODE HERE
 

# If the python node is executed as main process (sourced directly)
if __name__ == '__main__':
  try:
      ar_nav = Tag_nav()
      rospy.spin()
  except rospy.ROSInterruptException:
      rospy.loginfo("Aruco_tag test finished.")  
