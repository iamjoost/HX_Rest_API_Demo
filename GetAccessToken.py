"""
This script is an example of how to use the HyperFlex REST API to get an authentication token of a HyperFlex Cluster.

When the script has this information, it can do a POST to get the tokens.

This solution is tested on HyperFlex 4.0.2a.

You can change this script to have it working anyway you want.
THIS SCRIPT IS NOT IDIOT PROOF

python GetAccessToken.py -h will give you the options. It is not advisable to use passwords in plain text.

Author : Joost van der Made 2020
IAmJoost.com
"""
import urllib3
import json
import sys
import getpass
import hxdef
import argparse


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

    return parser.parse_args(args)


# ========== MAIN ==============
urllib3.disable_warnings()

args = check_arg(sys.argv[1:])

hxip = args.hxip
hxuser = args.hxuser
hxpasswd = args.hxpasswd

if args.hxip == None:
    hxip = input("HyperFlex IP Address: ")

if args.hxuser == None:
    hxuser = input("HyperFlex UserName: ")

if args.hxpasswd == None:
    hxpasswd = getpass.getpass("Please enter the HyperFLex Password: ")

hxbearer = hxdef.get_hxtoken(hxip, hxuser, hxpasswd).json()
print ()
print("Access Token: ", hxbearer["access_token"])
print("Token Type: ", hxbearer["token_type"])
print("Refresh Token: ", hxbearer["refresh_token"])
