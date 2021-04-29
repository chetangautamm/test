#!/bin/bash

if [ "osm k8scluster-list | grep kubespray-cluster" ]
then
   echo "K8s Kubespray Cluster is Added Successfully"
else
   echo "K8s Kubespray Cluster is not Added Successfully"
fi
