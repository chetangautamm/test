#!/usr/bin/env python
# coding: utf-8

# In[350]:


import requests
import json
import sys
import logging
import os
import time
import urllib3

#Token Generation
url = "https://20.204.38.93:9999/osm"
def get_token(url):
    payload = json.dumps({ "username": "admin", "password": "admin", "project_id": "admin" })
    headers = { 'Accept': 'application/json', 'Content-Type': 'application/json' }
    r1 = requests.request("POST", url, headers=headers, data=payload, verify=False)
    if r1.status_code == 200:
        token = r1.json()['id']
        return token
    else:
        print("Failed to get token.")   

token = get_token(url+"/admin/v1/tokens")
print(f"token: {token}")


# In[351]:


#Checking VIM Accounts
def get_vim1_id(url, token):
    headers = { 'Authorization': f'Bearer {token}', 'Accept': 'application/json' }
    response = requests.request("GET", url, headers=headers, verify=False)
    vims = response.json()
    for vim in vims:
        if vim['name'] == "OpenstackR-1":
            return vim['_id']  

def get_vim2_id(url, token):
    headers = { 'Authorization': f'Bearer {token}', 'Accept': 'application/json' }
    response = requests.request("GET", url, headers=headers, verify=False)
    vims = response.json()
    for vim in vims:
        if vim['name'] == "OpenstackR-2":
            return vim['_id']  
        
vimId1 = get_vim1_id(url+f"/admin/v1/vims", token)
print(f"vimAccountId: {vimId1}")


vimId2 = get_vim2_id(url+f"/admin/v1/vims", token)
print(f"vimAccountId: {vimId2}")


# In[352]:


def get_opensips_ns_id(url, token):
    headers = { 'Authorization': f'Bearer {token}', 'Accept': 'application/json' }
    response = requests.request("GET", url, headers=headers, verify=False)
    data = response.json()
    for opensips in data:
        if opensips['name'] == "opensips":
            return opensips['name'],opensips['_id'] 

def get_uas_ns_id(url, token):
    headers = { 'Authorization': f'Bearer {token}', 'Accept': 'application/json' }
    response = requests.request("GET", url, headers=headers, verify=False)
    data = response.json()
    for uas in data:
        if uas['name'] == "uas":
            return uas['name'],uas['_id'] 
    
def get_uac_ns_id(url, token):
    headers = { 'Authorization': f'Bearer {token}', 'Accept': 'application/json' }
    response = requests.request("GET", url, headers=headers, verify=False)
    data = response.json()
    for uac in data:
        if uac['name'] == "uac":
            return uac['name'], uac['_id'] 

nsopensips = get_opensips_ns_id(url+f"/nslcm/v1/ns_instances_content", token)
print(f"ns_list: {nsopensips}")

nsuas = get_uas_ns_id(url+f"/nslcm/v1/ns_instances_content", token)
print(f"ns_list: {nsuas}")

nsuac = get_uac_ns_id(url+f"/nslcm/v1/ns_instances_content", token)
print(f"ns_list: {nsuac}")



# In[353]:


def get_instance_name(url, token):
    headers = { 'Authorization': f'Bearer {token}', 'Accept': 'application/json' }
    response = requests.request("GET", url, headers=headers, verify=False)
    data = response.json()
    for instance in data:
        print(instance['name'], instance['_id'])
nam = get_instance_name(url+f"/nslcm/v1/ns_instances_content", token)


# In[354]:


#Helm Repo 
def get_helm_repo(url, token):
    headers = { 'Authorization': f'Bearer {token}', 'Accept': 'application/json' }
    response = requests.request("GET", url, headers=headers, verify=False)
    data = response.json()
    for helm in data:
        if helm['name'] == "helm-osm":
            return helm['name'],helm['_id']   

repo = get_helm_repo(url+f"/admin/v1/k8srepos", token)
print(f"repo_name: {repo}")


# In[355]:


#K8sclusters
def get_k8s_cluster(url, token):
    headers = { 'Authorization': f'Bearer {token}', 'Accept': 'application/json' }
    response = requests.request("GET", url, headers=headers, verify=False)
    data = response.json()
    for k8s in data:
        if k8s['name'] == "kubespray-cluster":
            return k8s['name'],k8s['_id']  

def get_kubeadm_cluster(url, token):
    headers = { 'Authorization': f'Bearer {token}', 'Accept': 'application/json' }
    response = requests.request("GET", url, headers=headers, verify=False)
    data = response.json()
    for kube in data:
        if kube['name'] == "kubeadm-cluster":
            return kube['name'],kube['_id']   

cluster1 = get_k8s_cluster(url+f"/admin/v1/k8sclusters", token)
print(f"cluster_name: {cluster1}")

cluster2 = get_kubeadm_cluster(url+f"/admin/v1/k8sclusters", token)
print(f"cluster_name: {cluster2}")


# In[356]:


#NSD List
def get_opensips_nsd(url, token):
    headers = { 'Authorization': f'Bearer {token}', 'Accept': 'application/json' }
    response = requests.request("GET", url, headers=headers, verify=False)
    data = response.json()
    for opensips in data:
        if opensips['name'] == "jenkins_opensips-7_ns":
            return opensips['name'],opensips['_id']   

def get_uas_nsd(url, token):
    headers = { 'Authorization': f'Bearer {token}', 'Accept': 'application/json' }
    response = requests.request("GET", url, headers=headers, verify=False)
    data = response.json()
    for uas in data:
        if uas['name'] == "jenkins_uas-7_ns":
            return uas['name'],uas['_id']   

def get_uac_nsd(url, token):
    headers = { 'Authorization': f'Bearer {token}', 'Accept': 'application/json' }
    response = requests.request("GET", url, headers=headers, verify=False)
    data = response.json()
    for uac in data:
        if uac['name'] == "jenkins_uac-7_ns":
            return uac['name'],uac['_id']   

nsdname = get_opensips_nsd(url+f"/nsd/v1/ns_descriptors", token)
print(f"nsd_name: {nsdname}")


nsdname = get_uas_nsd(url+f"/nsd/v1/ns_descriptors", token)
print(f"nsd_name: {nsdname}")


nsdname = get_uac_nsd(url+f"/nsd/v1/ns_descriptors", token)
print(f"nsd_name: {nsdname}")


# In[357]:


#VNFD List
def get_opensips_vnfd(url, token):
    headers = { 'Authorization': f'Bearer {token}', 'Accept': 'application/json' }
    response = requests.request("GET", url, headers=headers, verify=False)
    data = response.json()
    for opensips in data:
        if opensips['id'] == "jenkins_opensips-7_knf":
            return opensips['id'], opensips['_id']   

def get_uas_vnfd(url, token):
    headers = { 'Authorization': f'Bearer {token}', 'Accept': 'application/json' }
    response = requests.request("GET", url, headers=headers, verify=False)
    data = response.json()
    for uas in data:
        if uas['id'] == "jenkins_uas-7_knf":
            return uas['id'], uas['_id']   

def get_uac_vnfd(url, token):
    headers = { 'Authorization': f'Bearer {token}', 'Accept': 'application/json' }
    response = requests.request("GET", url, headers=headers, verify=False)
    data = response.json()
    for uac in data:
        if uac['id'] == "jenkins_uac-7_knf":
            return uac['id'], uac['_id']   

vnfdname = get_opensips_vnfd(url+f"/vnfpkgm/v1/vnf_packages", token)
print(f"nsd_name: {vnfdname}")


vnfdname = get_uas_vnfd(url+f"/vnfpkgm/v1/vnf_packages", token)
print(f"nsd_name: {vnfdname}")


vnfdname = get_uac_vnfd(url+f"/vnfpkgm/v1/vnf_packages", token)
print(f"nsd_name: {vnfdname}")


# In[ ]:





# In[ ]:




