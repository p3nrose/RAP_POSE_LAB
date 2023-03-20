This project is based on ROS Noetic and covers the topics of the RAP course lab: **RAP_POSE_LAB**

You have three options to work with the project as detailed below.

## On the K8S cluster provided by the course (recommended)

### 1. Requirements

In order to be able to deploy the container on the K8S cluster, you will need:
- kubectl installed on your system (install instructions here: https://kubernetes.io/docs/tasks/tools/)
- kubernetes config file containing your credentials (downloadable from the k8s cluster https://robopaas.dev) saved where kubectl expects it to be on your system (by default, kubectl configuration is located at ~/.kube/config)

#### Note for Windows users

Windows users may use WSL to run Ubuntu on their system (install instructions here: https://learn.microsoft.com/en-us/windows/wsl/install).
Once installed Ubuntu can be installed/run with the following commands:

    $ wsl --install -d Ubuntu
    $ wsl -d Ubuntu
    
In Ubuntu you will have to proceed with the two steps listed in the Requirements section above.

### 2. Deployment

Steps to deploy the container:
1. Clone the repo on your machine or download the rap-lab-deploy.sh / rap-lab-remove.sh scripts and the rap-2023-lab-deployment.yaml file  to your machine
2. Launch rap-lab-deploy.sh it within a bash terminal providing your groupID, and the password that will be used to access the container

For example:

    $ ./rap-lab-deploy.sh 7 myPassWD456

What will happen:
- The script will create a k8s "deployment" with a single pod running your container
- The password to access your container through your browser and a VNC server will be set
- Your container will mount in the directory /home/ros/rap a pre-existing persistent volume where you will be able to clone the RAP projects. This is to prevent you from accidentally losing your code once you shut off the container
- Your container will be accessible to your browser through a pre-existing k8s ingress at a group-specific URL, e.g.: https://rap-2023-7.robopaas.dev/

#### Security Notice for K8S Cluster
We are entrusting you with the possibility to run remotely accessible services on a cluster, so **please use this capabilities responsibly**. Notice that **any violation of cluster usage terms will result in termination of your access credentials and reporting to the school**.

Within your group you will share a forked copy of RAP lab repositories. In order to push your code without sharing your personal credentials with other group members, you can access your containers from a shell using the exec command, e.g., for group 7:

    $ kubectl exec -n rap-2023-7 -it <pod-name> -- bash
    
You can see the name of your pod (collection of co-located containers) in your group namespace with e.g., for group 7:

    $ kubectl -n rap-2023-7 get pod

### 3. Removing the deployed container

You can remove the deployment you created with the rap-lab-remove.sh script and your group ID, e.g.:

    $ ./rap-lab-remove.sh 7

-------------
## On your own laptop (Any OS supporting docker compose)

When working with your own laptop, you can launch the containers using docker-compose with the following command:

    docker-compose up

This will launch two containers, one with the ROS Noetic environment installed for you to work on, and one for novnc (the GUI) which you can access through your browser at: http://127.0.0.1/vnc.html.

In another terminal, you can access the ROS container with:

    docker exec -it rap_intro_lab_ros_1 bash
  
Double check the container name using docker ps command.

From that console you can launch the scripts of the lab (e.g., roslaunch ...)

*NOTE:* the ZHAW VPN client gets in the way of the networking between the containers. If you experience issues try disconnecting from the VPN and restarting the composition.

-------------
## On your own laptop (any Linux with Xserver and docker)

You may also want to start a container without novnc, but connecting to a *local running Xserver instance*. For this you can use the following command:

    ./run_cpu_local_xserver.sh

Note that the xhost needs to be correctly set in order to make it work correctly. (xhost+ would do the trick)
