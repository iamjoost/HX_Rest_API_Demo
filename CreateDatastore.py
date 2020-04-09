"""
This script is an example of how to use the HyperFlex REST API to create a Datastores of a HyperFlex Cluster.
It will get the token and find the UUID of the cluster.
When the script has this information, it can do a POST to create  the Datastore

This solution is tested on HyperFlex 4.0.2a.

You can change this script to have it working anyway you want.
THIS SCRIPT IS NOT IDIOT PROOF

python CreateDatastore.py -h will give you the options. It is not advisable to use passwords in plain text.

Author : Joost van der Made 2020
IAmJoost.com
"""

import hxdef
import urllib3
import sys
import argparse
import getpass

################## FUNCTIONS ################
# Getting the parameters
def check_arg(args=None):
    parser = argparse.ArgumentParser(description='HyperFlex Get Authentication Token.')
    parser.add_argument('--hxip',
                        help='HyperFlex ip',
                        )
    parser.add_argument('--hxpasswd',
                        help='HyperFlex Cluster Password',
                        )
    parser.add_argument('--hxuser',
                        help='hx user name',
                        )
    parser.add_argument('--dsname',
                        help='Datastore name',
                        )
    parser.add_argument('--dssize',
                        help='Datastore Size in Gb',
                        )
    parser.add_argument('--dsblock',
                        help='Blocksize. Default is 8K (8192). 4K has a value of 4096.',
                        default=8192
                        )

    return parser.parse_args(args)

################## MAIN #####################
urllib3.disable_warnings()

args = check_arg(sys.argv[1:])

hxip = args.hxip
hxuser = args.hxuser
hxpasswd = args.hxpasswd
dsname = args.dsname
dssize = args.dssize
dsblock = args.dsblock

if args.hxip == None:
    hxip = input("HyperFlex IP Address: ")

if args.hxuser == None:
    hxuser = input("HyperFlex UserName: ")

if args.hxpasswd == None:
    hxpasswd = getpass.getpass("Please enter the HyperFLex Password: ")

if args.dsname == None:
    dsname = input("Datastore Name: ")

if args.dssize == None:
    dssize = input("Datastore Size in Gb: ")


hxbearer = hxdef.get_hxtoken(hxip, hxuser, hxpasswd).json()

# Get Datastores from Cluster UUID
hxuuid = hxdef.get_hxuuid(hxip,hxbearer['access_token'])

#Create DS
dscreated = hxdef.create_ds (hxip,hxbearer['access_token'],hxuuid,dsname,dssize,dsblock)
if dscreated:
    print("Datastore is created")
else:
    print ("Datastore is not created.")