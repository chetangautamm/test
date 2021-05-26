#/bin/bash

#Deleting NS instances
var1=$(osm ns-list | grep  -P '(^|\s)\Kopensips(?=\s|$)' | awk '{print $2}');
var2="opensips"
if [ "$var1" = "$var2" ]
then
   echo "Opensips NS Instance is present.Remove It!!"
   osm ns-delete opensips 
else
   echo "Opensips NS Instance is not present!!"
fi

sleep 5 

var3=$(osm ns-list | grep -P '(^|\s)\Kuas(?=\s|$)' | awk '{print $2}');
var4="uas"
if [ "$var3" = "$var4" ]
then
   echo "UAS NS Instance is present.Remove It!!"
   osm ns-delete uas 
else
   echo "UAS NS Instance is not present!!"
fi

sleep 5
var5=$(osm ns-list | grep -P '(^|\s)\Kuac(?=\s|$)' | awk '{print $2}');
var6="uac"
if [ "$var5" = "$var6" ]
then
   echo "UAC NS Instance is present.Remove It!!"
   osm ns-delete uac 
else
   echo "UAC NS Instance is not present!!"
fi

sleep 5

var25=$(osm ns-list | grep  -P '(^|\s)\Kopensips-prod(?=\s|$)' | awk '{print $2}');
var26="opensips-prod"
if [ "$var25" = "$var26" ]
then
   echo "Opensips-Prod NS Instance is present.Remove It!!"
   osm ns-delete opensips-prod 
else
   echo "Opensips-Prod NS Instance is not present!!"
fi

#Deleting Kubernetes Cluster
var7=$(osm k8scluster-list | grep -P '(^|\s)\Kkubespray-cluster(?=\s|$)' | awk '{print $2}');
var8="kubespray-cluster"
if [ "$var7" = "$var8" ]
then
   echo "Kubernetes Cluster is present.Remove It!!"
   osm k8scluster-delete kubespray-cluster --force
else
   echo "Kubernetes Cluster is not present!!"
fi

var23=$(osm k8scluster-list | grep -P '(^|\s)\Kkubeadm-cluster(?=\s|$)' | awk '{print $2}');
var24="kubeadm-cluster"
if [ "$var23" = "$var24" ]
then
   echo "Kubeadm Cluster is present.Remove It!!"
   osm k8scluster-delete kubeadm-cluster --force
else
   echo "Kubeadm Cluster is not present!!"
fi


#Deleting Helm Repository
var9=$(osm repo-list | grep -P '(^|\s)\Khelm-osm(?=\s|$)' | awk '{print $2}');
var10="helm-osm"
if [ "$var9" = "$var10" ]
then
   echo "Helm Repository is present.Remove It!!"
   osm repo-delete helm-osm --force
else
   echo "Helm Repository is not present!!"
fi

sleep 5

#Deleting NSD of Jenkins
var17=$(osm nsd-list | grep -P '(^|\s)\Kjenkins_opensips-7_ns(?=\s|$)' | awk '{print $2}');
var18="jenkins_opensips-7_ns"
if [ "$var17" = "$var18" ]
then
   echo "Opensips NSD is present.Remove It!!"
   osm nsd-delete jenkins_opensips-7_ns
else
   echo "Opensips NSD is not present!!"
fi

var19=$(osm nsd-list | grep -P '(^|\s)\Kjenkins_uas-7_ns(?=\s|$)' | awk '{print $2}');
var20="jenkins_uas-7_ns"
if [ "$var19" = "$var20" ]
then
   echo "UAS NSD is present.Remove It!!"
   osm nsd-delete jenkins_uas-7_ns
else
   echo "UAS NSD is not present!!"
fi

var21=$(osm nsd-list | grep -P '(^|\s)\Kjenkins_uac-7_ns(?=\s|$)' | awk '{print $2}');
var22="jenkins_uac-7_ns"
if [ "$var21" = "$var22" ]
then
   echo "UAC NSD is present.Remove It!!"
   osm nsd-delete jenkins_uac-7_ns
else
   echo "UAC NSD is not present!!"
fi

sleep 5
#Deleting VNFD of Jenkins
var11=$(osm vnfd-list | grep -P '(^|\s)\Kjenkins_opensips-7_knf(?=\s|$)' | awk '{print $2}');
var12="jenkins_opensips-7_knf"
if [ "$var11" = "$var12" ]
then
   echo "Opensips VNFD is present.Remove It!!"
   osm vnfd-delete jenkins_opensips-7_knf
else
   echo "Opensips VNFD is not present!!"
fi

var13=$(osm vnfd-list | grep -P '(^|\s)\Kjenkins_uas-7_knf(?=\s|$)' | awk '{print $2}');
var14="jenkins_uas-7_knf"
if [ "$var13" = "$var14" ]
then
   echo "UAS VNFD is present.Remove It!!"
   osm vnfd-delete jenkins_uas-7_knf
else
   echo "UAS VNFD is not present!!"
fi

var15=$(osm vnfd-list | grep -P '(^|\s)\Kjenkins_uac-7_knf(?=\s|$)' | awk '{print $2}');
var16="jenkins_uac-7_knf"
if [ "$var15" = "$var16" ]
then
   echo "UAC VNFD is present.Remove It!!"
   osm vnfd-delete jenkins_uac-7_knf
else
   echo "UAC VNFD is not present!!"
fi


#Verifying Deletion of services
osm ns-list
osm k8scluster-list
osm repo-list
osm nsd-list
osm vnfd-list

sleep 10
