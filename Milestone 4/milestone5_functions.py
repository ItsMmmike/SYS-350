# Milestone 5 Functions

# Import functions from milestone 4
from pyVim.connect import SmartConnect
from pyVmomi import vim

# Function retrives all available vm info from vcenter
def vmData(si):
  content = si.RetrieveContent()
  container = content.viewManager.CreateContainerView(content.rootFolder, [vim.VirtualMachine], True)
  return container.view

# Function used to prompt users to select an available Vcenter VM
#   - Returns VM Name if found, returns "False" if not
def selectVM(si):

    # Retrieve VM Data
    vms = vmData(si)
    # Lists all available VMs
    for vm in vms:
        print(vm.name)

    # Prompt users to input a vm name
    print("")
    print("====================")
    search = input("Please select a VM: ")

    if search == "":
        search = None

    # Loop used to find/return selected VM
    for vm in vms:

        # Initial check for blank entry
        if search == None:
            print("No VM selected, please try again")
            return 0 # Do we want to check if this route works?

        # Return VM Name if match found
        if vm.name == search:
            return vm
    
    # Catch used if no matches were found
    else:
        print("VM not found, please try again") 
        return False # Default response if function is unable to locate vm
      

def powerOffVM(si):
    vm = selectVM(si)

    # Check to see if vm is already powered off

    if vm != False:
        vm.PowerOffVM_Task()
        print(str(vm.name)+" powering off")


def powerOnVM(si):
    # Query list of vms here

    # vm.PowerOnVM_Task()
    print("hello world")

def takeVMSnapshot(si):
    # Query list of vms here

    # Ask user to provide a name for this snapshot

    #vm.CreateSnapshotEx_Task(name=$snapshotName, memory=False)
    print("hello world")

def restoreVMSnapshot(si):
    # Query list of vms here

    # Ask user if they are sure they want to revert VM to latest snapshot (y/n)

    # Run task

    # Inform user that task is complete
    
    print("hello world")

def cloneVM(si):
    # Query list of vms available to clone
    print("test")

def removeVM(si):
    # Query list of vms available to be removed
    # (The current selected VM is: <VM Name> --> Ask user if they are sure they want to delete the selected vm.
    print("test")


def milestone5Menu():
    menuStatus = True
    while menuStatus == True:
        print("================================")
        print("Welcome to the VM Operation Menu!")
        print("")
        print("[1] - Power On VM")
        print("[2] - Power Off VM")
        print("[3] - Take VM Snapshot")
        print("[4] - Restore VM Snapshot")
        print("[5] - Clone a VM")
        print("[6] - Delete a VM")
        print("[7] - Exit to Main Menu")
        print("")
        selection = input("Please select an option from the menu above: ")

        if selection == "1":
            print("cool test")

        if selection == "2":
            print("cool test")
        
        if selection == "3":
            print("cool test")

        if selection == "4":
            print("cool test")

        if selection == "5":
            print("cool test")

        if selection == "6":
            print("cool test")

        if selection == "7":
            print("Exiting Script")
            menuStatus = False

        # Catch used to respond to unexpected inputs
        else:
            print("Invalid option, please try again")
            continue

