"""
This script is an example of how to use the HyperFlex REST API to List the Datastores of a HyperFlex Cluster.
It will get the token and find the UUID of the cluster.
When the script has this information, it can do a GET for the Datastores

This solution is tested on HyperFlex 4.0.2a.

You can change this script to have it working anyway you want.
THIS SCRIPT IS NOT IDIOT PROOF

python ListDatastore.py -h will give you the options. It is not advisable to use passwords in plain text.

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
    '''Collect the args'''
    parser = argparse.ArgumentParser(description='List the datastores of a HyperFlex cluster.')
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
    parser.add_argument('--hxtoken',
                        help='HX API Token',
                        )

    return parser.parse_args(args)

################## MAIN #####################
urllib3.disable_warnings() #Disable warnings when you're not working with certificates.

# Bind the args to variables. If it is not specified, ask about the needed info.
args = check_arg(sys.argv[1:])
hxip = args.hxip
hxuser = args.hxuser
hxpasswd = args.hxpasswd
token = args.hxtoken

if args.hxip == None:
    hxip = input("HyperFlex IP Address: ")

if args.hxuser == None:
    hxuser = input("HyperFlex UserName: ")

if args.hxpasswd == None:
    hxpasswd = getpass.getpass("Please enter the HyperFLex Password: ")

if args.hxtoken == None:
    # Get the Token.
    hxbearer = hxdef.get_hxtoken(hxip, hxuser, hxpasswd).json()
    token = hxbearer['access_token']

# Get the Cluster UUID
hxuuid = hxdef.get_hxuuid(hxip,token)

#Get Datastores from Cluster
ds = hxdef.get_ds(hxip,token,hxuuid)

#Print the name and Freespace of the Datastores.
for item in ds.json():
    print ("Datastore Name: ", item['dsconfig']['name'])
    print("Free Capacity", item['freeCapacityInBytes']/1024/1024/1024," GiB")

