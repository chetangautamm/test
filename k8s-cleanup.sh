#!/bin/bash

#Getting all deployments in OSM's namespace
kubectl get deployments -n d81d0c8e-dde0-464d-930c-79de5183b4db

#Deleting all deployments in Osm's namespace
kubectl delete deployments -n d81d0c8e-dde0-464d-930c-79de5183b4db --all

#Validating the deletion
kubectl get deployments -n d81d0c8e-dde0-464d-930c-79de5183b4db
