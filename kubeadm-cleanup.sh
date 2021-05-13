#!/bin/bash

#Capture Namespace
namespace=$(kubectl get ns | awk 'NR==2{print $1}');

#Getting all deployments in OSM's namespace
kubectl get deployments -n $namespace

#Deleting all deployments in Osm's namespace
kubectl delete deployments -n $namespace --all

#Validating the deletion
kubectl get deployments -n $namespace
