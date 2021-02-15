#!/usr/bin/env python
from __future__ import absolute_import
from __future__ import print_function
from datetime import datetime
import csv
import sys
import configparser

import duo_client
from six.moves import input

ARGS = len(sys.argv) - 1
#if ( ARGS != 1 ):
#   print ("Need passing the username")
#   exit()

#USERID = sys.argv[1]
#print ("USERNAME is %s" % (USERNAME))

config = configparser.ConfigParser(allow_no_value=True)
config.read('duo_init.cfg')

IKEY = config["duo"]["key"]
SKEY = config["duo"]["secret"]
HOST = config["duo"]["host"]


# Configuration and information about objects to create.
admin_api = duo_client.Admin(
    ikey=IKEY,
    skey=SKEY,
    host=HOST,

)

# Retrieve user info from API:
#users = admin_api.get_users_by_name(username=USERNAME)
#users= admin_api.get_authentication_log /admin/v2/logs/authentication
authlogs= admin_api.get_authentication_log(api_version=1)

# Print CSV of username, phone number, phone type, and phone platform:
#
# (If a user has multiple phones, there will be one line printed per
# associated phone.)
reporter = csv.writer(sys.stdout)
print("[+] Report of all users and associated phones:")
reporter.writerow(('Time', 'UserName', 'Factor', 'IP', 'Result'))
for outlog in authlogs:
        reporter.writerow([
                datetime.fromtimestamp(outlog["timestamp"]),
                outlog["username"],
                outlog["factor"],
                outlog["ip"],
                outlog["result"],
                outlog["location"]["city"],
        ])
