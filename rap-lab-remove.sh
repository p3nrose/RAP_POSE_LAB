#! /usr/bin/env bash
if [ $# != 1 ]; then
    echo "usage: rap-lab-remove.sh <group-id>"
    exit
else
    echo
    echo "Removing RAP lab from ZHAW InIT Kubernetes Cluster..."
    echo
    GROUPNO=${1}
    NAMESPACE="class-rap-2022-${GROUPNO}"
    kubectl delete -n ${NAMESPACE} deploy rap-2022-${GROUPNO}-deployment
fi
