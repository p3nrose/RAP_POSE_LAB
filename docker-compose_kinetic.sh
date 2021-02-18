version: '3'
services:
  ros:
    image: robopaas/rap-drive-lab
    hostname: rosdocked
    environment:
      - ROS_HOSTNAME=rosdocked
      - DISPLAY=novnc:0.0
    depends_on:
      - novnc
    command: roscore
    volumes:
      - $PWD:/home/ros/catkin_ws/src/rap_pose_lab/ 

  novnc:  
    image: robopaas/novnc:labs
    hostname: novnc
    environment:
      # Adjust to your screen size
      - DISPLAY_WIDTH= 1920
      - DISPLAY_HEIGHT= 1080
    shm_size: 2gb
    ports:
      - "443:8080"
