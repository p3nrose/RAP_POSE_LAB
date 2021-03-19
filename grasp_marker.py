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


class Tag_nav():
  '''Class for reacting to aruco_tags.'''

  def __init__(self):
   
      #ADD YOUR CODE HERE

    
  def callback_marker(self,data):

      #ADD YOUR CODE HERE



  def publish_camera_pose_from_marker(self, pose_tag, tag_id):

      #ADD YOUR CODE HERE




  def publish_grasp_pose(self, tag, tag_id):


   #ADD YOUR CODE HERE



  def gripper_client(self, value):
    p1 = rospy.Publisher('/gripper_left_controller/command', Float64, queue_size=1)
    p2 = rospy.Publisher('/gripper_right_controller/command', Float64, queue_size=1)
    rospy.sleep(0.5)
    p1.publish(-value)
    p2.publish(value)

  def callback_grasp(self,data):

      #ADD YOUR CODE HERE

      pose_goal = rotate_pose_msg_by_euler_angles(pose_goal.pose,  math.pi,  math.pi, math.pi / 2  )
      self.group.set_start_state_to_current_state()
      self.group.set_goal_tolerance(0.01)
      self.group.set_pose_target(pose_goal)
      print("planning ...")
      plan = self.group.plan()
      rospy.sleep(1)
      cont_plan_move = 0
      while ((len(plan.joint_trajectory.points) == 0) and (cont_plan_move < 10)):
          plan = self.group.plan()
          rospy.sleep(1)
          cont_plan_move += 1
      if (len(plan.joint_trajectory.points) != 0):
          result = self.group.execute(plan, wait=True)
      rospy.sleep(1)

      #ADD YOUR CODE HERE

      self.group.set_pose_target(pose_goal)
      print("planning ...")
      plan = self.group.plan()
      rospy.sleep(1)
      while ((len(plan.joint_trajectory.points) == 0) and (cont_plan_move < 10)):
          plan = self.group.plan()
          rospy.sleep(1)
          cont_plan_move += 1
      if (len(plan.joint_trajectory.points) != 0):
          result = self.group.execute(plan, wait=True)
      rospy.sleep(1)
      print("Object released")
 

if __name__ == '__main__': 
  try:
      ar_nav = Tag_nav()
      rospy.spin()
  except rospy.ROSInterruptException:
      rospy.loginfo("Aruco_tag test finished.")    

