#!/bin/bash

#Adding Kubernetes Cluster
osm k8scluster-add --creds kubeadm-config.yaml --version '1.21.0' --vim OpenstackR --description "Kubeadm Cluster" --k8s-nets '{"net1": "external"}' kubeadm-cluster

sleep 20
