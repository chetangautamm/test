#!/bin/bash

if [ "osm repo-list | grep helm-repo" ]
then
   echo "Helm Repository is Added Successfully"
else
   echo "Helm Repository is not Added Successfully"
fi

