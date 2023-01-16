#! /usr/bin/env bash

declare -i NODE_PORT=0

#map 0->99 to 31820 31919
map_group_to_port(){
    sourceRangeStart=0
    targetRangeStart=31820
    count=100

    requestNumber=$1

    numbers=( $(seq "$targetRangeStart" $((targetRangeStart+count-1)) ) )
    export NODE_PORT=$(( "${numbers[requestNumber-sourceRangeStart]}" ))
}

if [ $# != 2 ]; then
    echo "usage: rap-lab-deploy.sh <group-id> <password-to-be-set>"
    exit
else
    echo
    echo "Deploying RAP tools on ZHAW InIT Kubernetes Cluster..."
    echo

    export GROUPNO=${1}
    export PASSWD=${2}
    export NAMESPACE="rap-2023-${GROUPNO}"
    map_group_to_port $GROUPNO 
    
    cat ./rap-2023-lab-deployment.yaml | envsubst | kubectl -n $NAMESPACE apply -f -
    
    echo
    echo "RAP tools deployed. Lab container should be accessible at"
    echo
    echo "https://rap-2023-${GROUPNO}.robopaas.dev"
    echo
    echo "Note that it may take up to 5 minutes before the system is up"
    echo
    echo "Happy RAPping!"
    echo

fi