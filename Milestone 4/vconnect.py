# vconnect starter
# https://github.com/rtgillen/SYS350-FA24/

import getpass
passw = getpass.getpass()
from pyVim.connect import SmartConnect
import ssl
s=ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
s.verify_mode=ssl.CERT_NONE
si=SmartConnect(host="vcenter.michael.local", user="michael-adm@michael.local", pwd=passw, sslContext=s)
aboutInfo=si.content.about
print(aboutInfo)
print(aboutInfo.fullName)

# Displaying Current API Version of vCenter
print(aboutInfo.apiVersion)