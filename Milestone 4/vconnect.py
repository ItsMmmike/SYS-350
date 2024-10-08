# Vconnect script adapted from:
# https://github.com/rtgillen/SYS350-FA24/

import getpass
passw = getpass.getpass()
from pyVim.connect import SmartConnect
import ssl
s=ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
s.verify_mode=ssl.CERT_NONE

# Retrieving User Login Config from json file
import json
with open('./Milestone 4/vcenter-conf.json') as a:
  data = json.load(a)
vcenterHost = data['vcenter'][0]['vcenterhost']
vcenterAdmin = data['vcenter'][0]['vcenteradmin']

si=SmartConnect(host=vcenterHost, user=vcenterAdmin, pwd=passw, sslContext=s)
aboutInfo=si.content.about
print(aboutInfo)
print(aboutInfo.fullName)

# Displaying Current API Version of vCenter
print(aboutInfo.apiVersion)

### Demo Script Requirements:
# 1. Read Vcenter Host + username from a file (vcenter-conf.json)

# Sources:
# https://w3schools.com/python/python_json.asp
# https://stackoverflow.com/questions/66588041/read-a-specific-value-from-a-json-with-python



# 2. Provide data on the current pyvmomi session (ex. Domain/Username, vcenter server + source IP address)
# --> **See Note on this deliverable element
# 3. Search Function that filters all vms in vcenter by name --> default returns all vms
# --> (if no vm found, inform user as such)
# 4. Expand functionality of part 3 to include metadata on VMs