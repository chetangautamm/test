#!/bin/bash

var1=$(osm k8scluster-list | grep -P '(^|\s)\Kkubeadm-cluster(?=\s|$)' | awk '{print $2}');
var2="kubeadm-cluster"
if [ "$var1" = "$var2" ]
then
   echo "Kubeadm Cluster is Added Successfully!!"
   osm k8scluster-list
else
   echo "Kubeadm Cluster is not Added!!"
fi
