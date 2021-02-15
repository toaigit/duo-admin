#!/usr/bin/env python
from __future__ import absolute_import
from __future__ import print_function
import csv
import sys
import configparser

import duo_client
from six.moves import input

# Configuration and information about objects to create.
config = configparser.ConfigParser(allow_no_value=True)
config.read('duo_init.cfg')

IKEY = config["duo"]["key"]
SKEY = config["duo"]["secret"]
HOST = config["duo"]["host"]

admin_api = duo_client.Admin(
    ikey=IKEY,
    skey=SKEY,
    host=HOST,
)

# Retrieve all user info from API:
users = admin_api.get_users()

# Print CSV of username, phone number, phone type, and phone platform:
#
# (If a user has multiple phones, there will be one line printed per
# associated phone.)
reporter = csv.writer(sys.stdout)
print("[+] Report of all users and associated phones:")
reporter.writerow(('Username', 'Phone Number', 'Phone Id', 'Type', 'Platform'))
for user in users:
    for phone in user["phones"]:
        reporter.writerow([
                user["username"],
                phone["number"],
                phone["phone_id"],
                phone["type"],
                phone["platform"],
        ])
