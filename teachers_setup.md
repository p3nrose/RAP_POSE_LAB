# Setup Steps for Lab (for teachers)

## Start arm + pi

Make sure any console on Pi uses the arm as master (use screen command)

Make sure pi is using wired connection by disbling wifi connection:

  sudo ifconfig wlan0 down
  
## Perform arm calibration with Niryo Client

Use your laptop and a direct connection for it

## Run the camera calibration script (on Pi)

In one of the screens start the camera (rs_camera.launch)

From icclab_grasping_niryo, run calibrate_camera.launch then run the static transformation publisher that is generated (see output on console)

# Configure the rosduct instances

Edit the arm_\*.yaml files in rosdcut/config to set up the correct WS endpoint for the group that will use the robot

# Launch the rosduct instances

Use tow different screens to launch the two client_arm_\*.launch files
Check that they are connected properly

Ask students if they see camera stream + robot position (remember they need to start rosbridge + moveit_rviz_fake_gripper.launch)
