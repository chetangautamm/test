#!/usr/bin/env python
# coding: utf-8

# In[8]:


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


# In[9]:


def helm_repo_add(url, token):
    headers = { 'Authorization': f'Bearer {token}', 'Accept': 'application/json', 'Content-Type': 'application/json' }
    payload = json.dumps({"name": "helm-osm","description": "Helm Repo for Opensips & Sipp","type": "helm-chart","url": "https://chetangautamm.github.io/osm-helm/"})
    response = requests.request("POST", url, headers=headers, data=payload, verify=False)
    return response.json()['id']

helm_repo_add(url+"/admin/v1/k8srepos",token)


# In[10]:


#Helm Repo 
def get_helm_repo(url, token):
    headers = { 'Authorization': f'Bearer {token}', 'Accept': 'application/json' }
    response = requests.request("GET", url, headers=headers, verify=False)
    data = response.json()
    for helm in data:
        if helm['name'] == "helm-osm":
            return 'Helm Repo Added Successfully' 
          
get_helm_repo(url+f"/admin/v1/k8srepos", token)


# In[ ]:





# In[ ]:




