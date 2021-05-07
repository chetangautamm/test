#!/bin/bash

var1=$(osm k8scluster-list | grep  -P '(^|\s)\K(kubespray-cluster?=\s|$)'| awk '{print $2}');
var2="kubespray-cluster"
if [ "$var1" = "$var2" ]
then
   echo "Kubernetes Cluster is Added Successfully!!"
   osm k8scluster-list
else
   echo "Kubernetes Cluster is not Added!!"
fi
