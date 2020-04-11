"""
Here are just some functions I am using for different HyperFlex REST API Scripts.

This solution is tested on HyperFlex 4.0.2a.

You can change this script to have it working anyway you want.
THIS SCRIPT IS NOT IDIOT PROOF

Author : Joost van der Made 2020
IAmJoost.com
"""

import requests
import json
import os


# Generate HyperFlex API Token.
def get_hxtoken(hxip, hxuser, hxpasswd):
    #payload = {'username': hxuser, 'password': hxpasswd, 'client_id': 'HxGuiClient', 'client_secret': 'Sunnyvale',
    #           'redirect_uri': 'http://localhost:8080/aaa/redirect/'}
    payload = {'username': hxuser, 'password': hxpasswd}

    headers = {
        "Content-type": "application/json",
        "Accept": "application/json"}

    url = 'https://' + hxip + '/aaa/v1/auth?grant_type=password'

    hxauth = requests.post(url, data=json.dumps(payload), headers=headers, verify=False)
    if hxauth.status_code == 201:
        return (hxauth)
    else:
        print ("There was an error getting the Token. Please try again in 15 minutes.")
        print ("You should be on HXDP 4.0 or Higher to run this script correctly. ")
        print("HTTP Error Code: ",hxauth.status_code)
        print ("Message: ",hxauth.text)

        os._exit(1)

# Get HyperFlex UUID of the Cluster
def get_hxuuid(hxip, hxtoken):
    headers = {
        "Content-type": "application/json",
        "Authorization": "Bearer " + hxtoken}

    url = 'https://' + hxip + '/coreapi/v1/clusters'
    response = requests.get(url, headers=headers, verify=False)
    for item in response.json():
        hxuuid = item['uuid']

    return hxuuid

#Get the Datastores from HyperFLex Cluster
def get_ds(hxip,hxtoken,hxuuid):
    headers = {
        "Content-type": "application/json",
        "Authorization": "Bearer " + hxtoken}

    url = "https://" + hxip + "/coreapi/v1/clusters/" + hxuuid + "/datastores"
    return(requests.get(url, headers=headers, verify=False))

#Create Datastore on the HyperFlex Cluster.
def create_ds(hxip,hxtoken,hxuuid,dsname,dssize,blocksize):
    payload = {"name": dsname, "sizeInBytes": dssize, "dataBlockSizeInBytes": blocksize}
    headers = {
        "Content-type": "application/json",
        "Authorization": "Bearer " + hxtoken}

    url = "https://" + hxip + "/coreapi/v1/clusters/" + hxuuid + "/datastores"
    hxds = requests.post(url, data=json.dumps(payload), headers=headers, verify=False)
    if hxds.status_code == 200:
        return True
    else:
        print ("There was an error")
        print ("Message: ",hxds.text)
        os._exit(1)

#Delete a Datastore on the HyperFLex Cluster
def delete_ds(hxip,hxtoken,hxuuid,dsuuid):
    headers = {
        "Content-type": "application/json",
        "Authorization": "Bearer " + hxtoken}

    url = "https://" + hxip + "/coreapi/v1/clusters/" + hxuuid + "/datastores/"+dsuuid
    hxds = requests.delete(url, headers=headers, verify=False)
    if hxds.status_code == 200:
        return True
    else:
        print ("There was an error")
        print ("Message: ",hxds.text)
        os._exit(1)
    return True