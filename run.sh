#!/usr/bin/env bash

export IMAGE_NAME=robopaas/rap-drive-lab

# Run the container with shared X11
#   --device=/dev/duo1:/dev/duo1\
# remove device mapping if docker complains
docker run\
  -h `hostname` \
  --privileged \
  --net=host \
  --device=/dev/dri \
  -e SHELL \
  -e DISPLAY \
  -e DOCKER=1 \
  -v "/tmp/.X11-unix:/tmp/.X11-unix:rw" \
  -v $PWD:/home/ros/catkin_ws/src/rap_pose_lab \
  -it $IMAGE_NAME $SHELL
