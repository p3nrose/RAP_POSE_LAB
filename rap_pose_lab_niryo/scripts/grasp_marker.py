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
from ar_track_alvar_msgs.msg import AlvarMarkers
from moveit_python.geometry import rotate_pose_msg_by_euler_angles, translate_pose_msg


class Tag_nav():
  '''Class for reacting to aruco_tags.'''

  def __init__(self):
    rospy.init_node('lab5_nav', anonymous=True)
    rospy.loginfo("Initialized Lab5 Node")
    self.move_arm = niryo_moveit("arm")
    self.gripper_pub1 = rospy.Publisher('/gripper_left_controller/command', Float64, queue_size=1)
    self.gripper_pub2 = rospy.Publisher('/gripper_right_controller/command', Float64, queue_size=1)
    # ADD YOUR CODE HERE (publishers, subscribers, tf_buffers...)

    
  def callback_marker(self, data):
    # ADD YOUR CODE HERE
   
    #pose = rotate_pose_msg_by_euler_angles(pose_transformed.pose,  math.pi,  math.pi, math.pi / 2  )
    # log and publish
    rospy.loginfo("Marker msg was: \n %s", data)
    rospy.loginfo("Transformed pose is: \n %s", grasp_pose)
    self.publish_grasp_pose(grasp_pose)
    # open gripper
    self.gripper_client(-0.5)
    # send pose goal to arm
    self.move_arm.move_to(grasp_pose) 
    # close gripper
    self.gripper_client(0.1)
    
    # ADD YOUR CODE HERE to MOVE arm somewhere else and drop object
    


  def publish_grasp_pose(self, grasp_pose):
    # ADD YOUR CODE HERE

  def gripper_client(self, value):
    rospy.sleep(0.5)
    self.gripper_pub1.publish(-value)
    self.gripper_pub2.publish(value)
 

# If the python node is executed as main process (sourced directly)
if __name__ == '__main__':
  try:
      ar_nav = Tag_nav()
      rospy.spin()
  except rospy.ROSInterruptException:
      rospy.loginfo("Aruco_tag test finished.")  
