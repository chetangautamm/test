#!/bin/bash

var1=$(osm repo-list | grep helm-osm | awk '{print $2}');
var2="helm-osm"
if [ "$var1" = "$var2" ]
then
   echo "Helm Repository is Added Successfully!!"
   osm repo-list
else
   echo "Helm Repository is not Added!!"
fi

