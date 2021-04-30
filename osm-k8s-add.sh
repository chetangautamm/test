#!/bin/bash

osm k8scluster-add --creds kubespray-config.yaml --version '1.20.2' --vim devstack --description "Kubespray Cluster" --k8s-nets '{"net1": "external"}' kubespray-cluster

sleep 20
