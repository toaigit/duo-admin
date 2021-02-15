#!/usr/bin/env python
from __future__ import absolute_import
from __future__ import print_function
import csv
import sys
import configparser

import duo_client
from six.moves import input

ARGS = len(sys.argv) - 1
if ( ARGS != 1 ):
   print ("Need passing the PHONE_ID")
   exit()

PHONE_ID = sys.argv[1]
#print ("phone id is %s" % (PHONE_ID))

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

try:
   RC = admin_api.send_sms_activation_to_phone(phone_id=PHONE_ID)
except RuntimeError:
   print ("RuntimeError when sending sms message")
