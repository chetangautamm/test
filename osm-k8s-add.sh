#!/bin/bash

#Adding Kubernetes Cluster
osm k8scluster-add --creds kubespray-config.yaml --version '1.20.2' --vim OpenstackR-1 --description "Kubespray Cluster" --k8s-nets '{"net1": "external"}' kubespray-cluster

sleep 20
