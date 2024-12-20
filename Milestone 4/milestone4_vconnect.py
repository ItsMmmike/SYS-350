# Milestone 4 Vconnect script

import getpass
passw = getpass.getpass()
from pyVim.connect import SmartConnect
from pyVmomi import vim
import ssl
s=ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
s.verify_mode=ssl.CERT_NONE

# Retrieving User Login Config from json file
import json
with open('./Milestone 4/vcenter-conf.json') as a:
  data = json.load(a)
vcenterHost = data['vcenter'][0]['vcenterhost']
vcenterAdmin = data['vcenter'][0]['vcenteradmin']
# Session Token
si=SmartConnect(host=vcenterHost, user=vcenterAdmin, pwd=passw, sslContext=s)

# Importing Functions from Milestone 5
import milestone5_functions
m5 = milestone5_functions

# Function used to print out information/elements from the vcenter "aboutInfo" object
def vCenterInfo(si):
  aboutInfo = si.content.about.fullName
  print("Current vCenter Version: "+aboutInfo)

### Demo Script Requirements:
# 1. Read Vcenter Host + username from a file (vcenter-conf.json)

# Sources:
# https://w3schools.com/python/python_json.asp
# https://stackoverflow.com/questions/66588041/read-a-specific-value-from-a-json-with-python

# 2. Provide data on the current pyvmomi session (ex. Domain/Username, vcenter server + source IP address)
# --> **See Note on this deliverable element

# Provides info on the current pyvmomi session
def getSessionInfo(si):
  sessionInfo = si.content.sessionManager.currentSession
  
  # Vars used to stored the gathered session info
  domainUser = sessionInfo.userName
  Source_IP =  sessionInfo.ipAddress

  #  results to terminal
  print("The current logged in user is "+domainUser+" from "+Source_IP+" at "+vcenterHost)


# 3. Search Function that filters all vms in vcenter by name --> default returns all vms
# --> (if no vm found, inform user as such)

# Sources:
# https://www.ntpro.nl/blog/archives/3751-Mastering-vCenter-Operations-with-Python-A-Script-to-Manage-Your-VMs.html

# Function used to search for a specifc VM based on user input query
# >> If no search query is specified, function displays all VMs
def vmInfo(si, search=None):

  # Retrieves all available vm info from vcenter
  content = si.RetrieveContent()
  container = content.viewManager.CreateContainerView(content.rootFolder, [vim.VirtualMachine], True)
  vms = container.view

  # Check to see if search query is empty --> displays all VMs in that is the case
  if search == None:
    print(" ")
    print("List of available VMs:")
    print("======================")
    for vm in vms:
      print("")
      print("=====")
      print("VM Name: "+ str(vm.name)) # Displays system name
      print("Power State: "+str(vm.runtime.powerState)) # Displays current system power state
      print("System Memory: "+str((vm.config.hardware.memoryMB)/1024)) # Displays number of sys memory in MB
      print("CPU Number: "+str(vm.config.hardware.numCPU)) # Displays number of sys CPU cores
      print("IP Address: "+str(vm.guest.ipAddress)) # Displays current IP Address
  
  # Runs query search if there is a provided "search" term
  else:
    print(" ")
    print("VM Query Result:")
    print("======================")

    # Loop used to determine if the requested vm can be found in vcenter
    for vm in vms:
      if vm.name == search:     
        print("VM Name: "+str(vm.name))
        print("Power State: "+str(vm.runtime.powerState))
        print("System Memory: "+str((vm.config.hardware.memoryMB)/1024))
        print("CPU Number: "+str(vm.config.hardware.numCPU))
        print("IP Address: "+str(vm.guest.ipAddress))
        break
    # Informs user if the VM cannot be found
    else:
      print("No VMs found with query "+search+". Please try again.")

# Menu Function used to prompt the user what functions they would like to run
def menu():
  menuStatus = True
  while menuStatus == True:
    print("")
    print("[1] - Display Vcenter Version")
    print("[2] - Display Session Info")
    print("[3] - Search VMs")
    print("[4] - VM Operations")
    print("[5] - Exit")
    print("")
    selection = input("Please select an option from the menu above: ")
    
    # Displays the current vCenter Version
    if selection == "1":
      print("")
      vCenterInfo(si)
      continue

    # Displays the info on the current Pyvmomi Session
    if selection == "2":
      print("")
      getSessionInfo(si)
      continue

    # Search function used to filter VMs by name, displays all VMs if no filter was provided
    if selection == "3":
      # Asks for user input
      searchVM = input("Please input a vm name to search (Leave blank to view all VMs): ")

      # Checks to see if the user left field blank --> then lists all vms
      if searchVM == "":
        vmInfo(si)
        continue

      # If user inputs query --> run vm search and display findings if possible
      else:
        vmInfo(si, searchVM)
        continue

    if selection == "4":
      m5.milestone5Menu(si)
      continue

    if selection == "5":
      print("Exiting Script")
      menuStatus = False

    # Catch used to respond to unexpected inputs
    else:
      print("Invalid option, please try again")
      continue

# Allows the Menu Script to run on startup
menu()

# 4. Expand functionality of part 3 to include metadata on VMs
#    >> Already included in the "vmInfo" function (*See above for more info)


# Also used W3Schools.com as reference --> Very useful resource for referencing how to use python code syntax
