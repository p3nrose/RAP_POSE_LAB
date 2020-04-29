#!/usr/bin/env python2

import rospy
import tf

import numpy as np
# from scipy.spatial.transform import Rotation as R
from tf.transformations import quaternion_matrix


if __name__ == '__main__':
#ROS translates first and then rotates
#By running tf tf_echo we found the translations from summit_xl_base_footprint to summit_xl_base_link to summit_xl_front_laser_base_link to summit_xl_front_laser_link


	# summit_xl_base_footprint to summit_xl_base_link
	trans1 = [0, 0, 0.125]
	q1 = [0, 0, 0, 1]
	# Rotation matrix of the quat
	R1 = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
	print R1

	# summit_xl_base_link to summit_xl_front_laser_base_link
	trans2 = [0.356, -0.251, 0.157]
	q2 = [0, 0, -0.383, 0.924]
	# Rotation matrix of the quat
	R2 = np.array([[0.7067584,  0.7074550,  0.0000000], [-0.7074550,  0.7067584,  0.0000000], [0.0000000,  0.0000000,  1.0000000]])
	print R2

	# summit_xl_front_laser_base_link to summit_xl_front_laser_link
	trans3 = [0, 0, 0.055]
	Q = [0, 0, 0, 1]
	# Rotation matrix of the quat
	R3 = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
	print R3

	# Turn lists into vecrtors
	Trans1 = np.array(trans1)
	Trans2 = np.array(trans2)
	Trans3 = np.array(trans3)
	
	# with arrays we do elementwise addition which is what we need to do to calclulate the final translation of our examlpe

	## Multiply Matrices to find rotations ## 
	R12 = np.matmul(R1, R2)
	# Final rotation
	R123 = np.matmul(R12, R3)

	FinalTranslation = Trans1 + Trans2 + Trans3
	print FinalTranslation
	FinalRotation = R123	
	# Quat of final rotation Since all the other are the neutral quats we get:
	QF = [0, 0, -0.383, 0.924]
	# This is the same result we would get if used tf echo between the frames summit_xl_base_footprint and summit_xl_front_laser_link!
