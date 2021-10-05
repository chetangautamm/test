#!/usr/bin/env python
# coding: utf-8

# In[1]:


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
urllib3.disable_warnings()


# In[2]:


#Fetching NS Instance Ids
def get_opensips_ns_id(url, token):
    headers = { 'Authorization': f'Bearer {token}', 'Accept': 'application/json' }
    response = requests.request("GET", url, headers=headers, verify=False)
    data = response.json()
    for opensips in data:
        if opensips['name'] == "opensips":
            return opensips['_id'] 

def get_uas_ns_id(url, token):
    headers = { 'Authorization': f'Bearer {token}', 'Accept': 'application/json' }
    response = requests.request("GET", url, headers=headers, verify=False)
    data = response.json()
    for uas in data:
        if uas['name'] == "uas":
            return uas['_id'] 
    
def get_uac_ns_id(url, token):
    headers = { 'Authorization': f'Bearer {token}', 'Accept': 'application/json' }
    response = requests.request("GET", url, headers=headers, verify=False)
    data = response.json()
    for uac in data:
        if uac['name'] == "uac":
            return uac['_id']
        
def get_opensips_prod_id(url, token):
    headers = { 'Authorization': f'Bearer {token}', 'Accept': 'application/json' }
    response = requests.request("GET", url, headers=headers, verify=False)
    data = response.json()
    for opensips in data:
        if opensips['name'] == "opensips-prod":
            return opensips['_id'] 


opensipsId = get_opensips_ns_id(url+f"/nslcm/v1/ns_instances_content", token)
print(f"opensipsId: {opensipsId}")

opensipsProd = get_opensips_prod_id(url+f"/nslcm/v1/ns_instances_content", token)
print(f"opensipsProd: {opensipsProd}")

uasId = get_uas_ns_id(url+f"/nslcm/v1/ns_instances_content", token)
print(f"uasId: {uasId}")

uacId = get_uac_ns_id(url+f"/nslcm/v1/ns_instances_content", token)
print(f"uacId: {uacId}")


# In[3]:


#Deleting NS Instances
def delete_opensips_ns_instance(token, url):
    headers = { 'Authorization': f'Bearer {token}', 'Accept': 'application/json' }
    response = requests.request("DELETE", url, headers=headers, verify=False )
    if response.status_code == 204:
        print("Opensips NS instance deleted successfully.")
delete_opensips_ns_instance(token, url+f"/nslcm/v1/ns_instances_content/{opensipsId}")

def delete_uas_ns_instance(token, url):
    headers = { 'Authorization': f'Bearer {token}', 'Accept': 'application/json' }
    response = requests.request("DELETE", url, headers=headers, verify=False )
    if response.status_code == 204:
        print("Uas NS instance deleted successfully.")
delete_uas_ns_instance(token, url+f"/nslcm/v1/ns_instances_content/{uasId}")

def delete_uac_ns_instance(token, url):
    headers = { 'Authorization': f'Bearer {token}', 'Accept': 'application/json' }
    response = requests.request("DELETE", url, headers=headers, verify=False )
    if response.status_code == 204:
        print("Uac NS instance deleted successfully.")
delete_uac_ns_instance(token, url+f"/nslcm/v1/ns_instances_content/{uacId}")

def delete_opensips_prod_instance(token, url):
    headers = { 'Authorization': f'Bearer {token}', 'Accept': 'application/json' }
    response = requests.request("DELETE", url, headers=headers, verify=False )
    if response.status_code == 204:
        print("Opensips prod NS instance deleted successfully.")
delete_opensips_ns_instance(token, url+f"/nslcm/v1/ns_instances_content/{opensipsProd}")

time.sleep(15)


# In[4]:


#NSD List
def get_opensips_nsd(url, token):
    headers = { 'Authorization': f'Bearer {token}', 'Accept': 'application/json' }
    response = requests.request("GET", url, headers=headers, verify=False)
    data = response.json()
    for opensips in data:
        if opensips['name'] == "jenkins_opensips-7_ns":
            return opensips['_id']   

def get_uas_nsd(url, token):
    headers = { 'Authorization': f'Bearer {token}', 'Accept': 'application/json' }
    response = requests.request("GET", url, headers=headers, verify=False)
    data = response.json()
    for uas in data:
        if uas['name'] == "jenkins_uas-7_ns":
            return uas['_id']   

def get_uac_nsd(url, token):
    headers = { 'Authorization': f'Bearer {token}', 'Accept': 'application/json' }
    response = requests.request("GET", url, headers=headers, verify=False)
    data = response.json()
    for uac in data:
        if uac['name'] == "jenkins_uac-7_ns":
            return uac['_id']   

opensipsNsdId = get_opensips_nsd(url+f"/nsd/v1/ns_descriptors", token)
print(f"opensipsNsdId: {opensipsNsdId}")

uasNsdId = get_uas_nsd(url+f"/nsd/v1/ns_descriptors", token)
print(f"uasNsdId: {uasNsdId}")

uacNsdId = get_uac_nsd(url+f"/nsd/v1/ns_descriptors", token)
print(f"uacNsdId: {uacNsdId}")


# In[5]:


#Deleting nsd
def delete_opensips_nsd(token, url):
    headers = { 'Authorization': f'Bearer {token}', 'Accept': 'application/json' }
    response = requests.request("DELETE", url, headers=headers, verify=False )
    if response.status_code == 204:
        print("Opensips nsd deleted successfully.")
delete_opensips_nsd(token, url+f"/nsd/v1/ns_descriptors/{opensipsNsdId}")

def delete_uas_nsd(token, url):
    headers = { 'Authorization': f'Bearer {token}', 'Accept': 'application/json' }
    response = requests.request("DELETE", url, headers=headers, verify=False )
    if response.status_code == 204:
        print("Uas nsd deleted successfully.")
delete_uas_nsd(token, url+f"/nsd/v1/ns_descriptors/{uasNsdId}")

def delete_uac_nsd(token, url):
    headers = { 'Authorization': f'Bearer {token}', 'Accept': 'application/json' }
    response = requests.request("DELETE", url, headers=headers, verify=False )
    if response.status_code == 204:
        print("Uac nsd deleted successfully.")
delete_uac_nsd(token, url+f"/nsd/v1/ns_descriptors/{uacNsdId}")

time.sleep(10)


# In[6]:


#VNFD List
def get_opensips_vnfd(url, token):
    headers = { 'Authorization': f'Bearer {token}', 'Accept': 'application/json' }
    response = requests.request("GET", url, headers=headers, verify=False)
    data = response.json()
    for opensips in data:
        if opensips['id'] == "jenkins_opensips-7_knf":
            return opensips['_id']   

def get_uas_vnfd(url, token):
    headers = { 'Authorization': f'Bearer {token}', 'Accept': 'application/json' }
    response = requests.request("GET", url, headers=headers, verify=False)
    data = response.json()
    for uas in data:
        if uas['id'] == "jenkins_uas-7_knf":
            return uas['_id']   

def get_uac_vnfd(url, token):
    headers = { 'Authorization': f'Bearer {token}', 'Accept': 'application/json' }
    response = requests.request("GET", url, headers=headers, verify=False)
    data = response.json()
    for uac in data:
        if uac['id'] == "jenkins_uac-7_knf":
            return uac['_id']   

opensipsVnfdId = get_opensips_vnfd(url+f"/vnfpkgm/v1/vnf_packages", token)
print(f"opensipsVnfdId: {opensipsVnfdId}")


uasVnfdId = get_uas_vnfd(url+f"/vnfpkgm/v1/vnf_packages", token)
print(f"uasVnfdId: {uasVnfdId}")


uacVnfdId = get_uac_vnfd(url+f"/vnfpkgm/v1/vnf_packages", token)
print(f"uacVnfdId: {uacVnfdId}")


# In[7]:


#Deleting vnfd
def delete_opensips_vnfd(token, url):
    headers = { 'Authorization': f'Bearer {token}', 'Accept': 'application/json' }
    response = requests.request("DELETE", url, headers=headers, verify=False )
    if response.status_code == 204:
        print("Opensips vnfd deleted successfully.")
delete_opensips_vnfd(token, url+f"/vnfpkgm/v1/vnf_packages/{opensipsVnfdId}")

def delete_uas_vnfd(token, url):
    headers = { 'Authorization': f'Bearer {token}', 'Accept': 'application/json' }
    response = requests.request("DELETE", url, headers=headers, verify=False )
    if response.status_code == 204:
        print("Uas vnfd deleted successfully.")
delete_uas_vnfd(token, url+f"/vnfpkgm/v1/vnf_packages/{uasVnfdId}")

def delete_uac_vnfd(token, url):
    headers = { 'Authorization': f'Bearer {token}', 'Accept': 'application/json' }
    response = requests.request("DELETE", url, headers=headers, verify=False )
    if response.status_code == 204:
        print("Uac vnfd deleted successfully.")
delete_uac_vnfd(token, url+f"/vnfpkgm/v1/vnf_packages/{uacVnfdId}")

time.sleep(10)


# In[8]:


#Helm Repo Id Get
def get_helm_repo(url, token):
    headers = { 'Authorization': f'Bearer {token}', 'Accept': 'application/json' }
    response = requests.request("GET", url, headers=headers, verify=False)
    data = response.json()
    for helm in data:
        if helm['name'] == "helm-osm":
            return helm['_id']   

helmId = get_helm_repo(url+f"/admin/v1/k8srepos", token)


# In[9]:


#Delete Helm Repo
def delete_helm_repo(token, url):
    headers = { 'Authorization': f'Bearer {token}', 'Accept': 'application/json' }
    response = requests.request("DELETE", url, headers=headers, verify=False )
    if response.status_code == 204:
        print("Helm Repo deleted successfully.")
        
delete_helm_repo(token, url+f"/admin/v1/k8srepos/{helmId}")

