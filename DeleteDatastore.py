"""
This script is an example of how to use the HyperFlex REST API to delete a Datastores of a HyperFlex Cluster.
It will get the token and find the UUID of the cluster.
When the script has this information, it can do a DELETE of the Datastores

This solution is tested on HyperFlex 4.0.2a.

You can change this script to have it working anyway you want.
THIS SCRIPT IS NOT IDIOT PROOF

python DeleteDatastore.py -h will give you the options. It is not advisable to use passwords in plain text.

Author : Joost van der Made 2020
IAmJoost.com
"""

import hxdef
import urllib3
import sys
import argparse
import os
import getpass


################## FUNCTIONS ################
# Getting the parameters
def check_arg(args=None):
    parser = argparse.ArgumentParser(description='HyperFlex Get Authentication Token.')
    parser.add_argument('--hxip',
                        help='HyperFlex ip',
                        # required='True', # Is argument required ?
                        # default='10.1.15.13'
                        )
    parser.add_argument('--hxpasswd',
                        help='HyperFlex Cluster Password',
                        )
    parser.add_argument('--hxuser',
                        help='hx user name',
                        # default='root'
                        )
    parser.add_argument('--dsname',
                        help='Datastore name',
                        # default='root'
                        )

    return parser.parse_args(args)

################## MAIN #####################
urllib3.disable_warnings()

args = check_arg(sys.argv[1:])

hxip = args.hxip
hxuser = args.hxuser
hxpasswd = args.hxpasswd
dsname = args.dsname


if args.hxip == None:
    hxip = input("HyperFlex IP Address: ")

if args.hxuser == None:
    hxuser = input("HyperFlex UserName: ")

if args.hxpasswd == None:
    hxpasswd = getpass.getpass("Please enter the HyperFLex Password: ")

if args.dsname == None:
    dsname = input("Datastore Name: ")

hxbearer = hxdef.get_hxtoken(hxip, hxuser, hxpasswd).json()

# Get Datastores from Cluster UUID
hxuuid = hxdef.get_hxuuid(hxip,hxbearer['access_token'])



#Find Datastore UUID
ds = hxdef.get_ds(hxip,hxbearer['access_token'],hxuuid)

for item in ds.json():
    if item['dsconfig']['name'] == dsname:
        dsuuid = item['uuid']
try:
    dsuuid
except NameError:
    dsuuid = None

#Get Datastores from Cluster
if dsuuid is None:
    print ("Datastore name is not found.")
    os._exit(1)

#Delete Datastore
dsdeleted = hxdef.delete_ds(hxip,token,hxuuid,dsuuid)
if dsdeleted:
    print("Datastore is deleted")
else:
    print ("Datastore is not deleted.")