#! /usr/bin/env bash
if [ $# != 3 ]; then
    echo "usage: rap-lab-deploy.sh <rap-key> <group-id> <password-to-be-set>"
    exit
else
    echo
    echo "Deploying RAP tools on ZHAW InIT Kubernetes Cluster..."
    echo

    export GPU_TOLERATION="gpu-taint-${1}"
    export GROUPNO=${2}
    export PASSWD=${3}
    export NAMESPACE="class-rap-2022-${GROUPNO}"

    cat ./rap-2022-lab-deployment.yaml | envsubst | kubectl -n $NAMESPACE apply -f -

    echo
    echo "RAP tools deployed. Lab container should be accessible at"
    echo
    echo "https://rap-2022-${GROUPNO}.k8s.init-lab.ch"
    echo
    echo "Note that it may take up to 1 minute before the system is up"
    echo
    echo "Happy RAPping!"
    echo

fi
