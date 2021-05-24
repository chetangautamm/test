#!/bin/bash

var1=$(osm k8scluster-list | grep -P '(^|\s)\Kkubespray-cluster(?=\s|$)' | awk '{print $2}');
var2="kubespray-cluster"
if [ "$var1" = "$var2" ]
then
   echo "Kubernetes Cluster is Already Present!!"
   osm k8scluster-list
else
   osm k8scluster-add --creds kubespray-config.yaml --version '1.20.2' --vim OpenstackR-1 --description "Kubespray Cluster" --k8s-nets '{"net1": "external"}' kubespray-   cluster
   sleep 20	  
   echo "Kubernetes Cluster is Added!!"
fi

#Adding Kubernetes Cluster
#osm k8scluster-add --creds kubespray-config.yaml --version '1.20.2' --vim OpenstackR-1 --description "Kubespray Cluster" --k8s-nets '{"net1": "external"}' kubespray-cluster

#sleep 20
