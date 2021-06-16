#!/usr/bin/env python
# coding: utf-8

# In[13]:


import requests
import json
import sys
import logging
import os
import time
import urllib3

#Token Generation
url = "https://52.172.254.152:9999/osm"
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


# In[14]:


def get_vim2_id(url, token):
    headers = { 'Authorization': f'Bearer {token}', 'Accept': 'application/json' }
    response = requests.request("GET", url, headers=headers, verify=False)
    vims = response.json()
    for vim in vims:
        if vim['name'] == "OpenstackR-2":
            return vim['_id']  
        
vimAccountId2 = get_vim2_id(url+f"/admin/v1/vims", token)
print(f"vimAccountId: {vimAccountId2}")


# In[15]:


def create_ns_instance(url, token, nsdId, vimAccountId):
    headers = { 'Authorization': f'Bearer {token}', 'Accept': 'application/json', 'Content-Type': 'application/json' }
    payload = json.dumps({ "nsName": "opensips-prod", "nsdId": f"{nsdId}", "vimAccountId": f"{vimAccountId2}", "nsDescription": "Generated by Automation" })
    response = requests.request("POST", url, headers=headers, data=payload, verify=False)
    print(response.text)
    return response.json()['id']


# In[16]:


def instantiate_ns(url, token, nsdId, vimAccountId):
    headers = { 'Authorization': f'Bearer {token}', 'Accept': 'application/json', 'Content-Type': 'application/json' }
    payload = json.dumps({ "nsName": "opensips-prod", "nsdId": f"{nsdId}", "vimAccountId": f"{vimAccountId2}", "nsDescription": "Generated by Automation" })
    response = requests.request("POST", url, headers=headers, data=payload, verify=False)
    print(response.text)
    return response.json()['id']


# In[17]:


def get_opensips_nsd(url, token):
    headers = { 'Authorization': f'Bearer {token}', 'Accept': 'application/json' }
    response = requests.request("GET", url, headers=headers, verify=False)
    data = response.json()
    for opensips in data:
        if opensips['name'] == "jenkins_opensips-7_ns":
            return opensips['_id']  


# In[18]:


nsdId = get_opensips_nsd(url+f"/nsd/v1/ns_descriptors", token)
print(f"nsdId: {nsdId}")

nsInstanceId = create_ns_instance(url+"/nslcm/v1/ns_instances", token, nsdId, vimAccountId2)

nsLcmOpOccId = instantiate_ns(url+f"/nslcm/v1/ns_instances/{nsInstanceId}/instantiate", token, nsdId, vimAccountId2)
