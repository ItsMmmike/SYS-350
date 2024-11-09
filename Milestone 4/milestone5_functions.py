# Milestone 5 Functions

# Import pyvmomi + auth token from Milestone 4
from pyVmomi import vim
from pyVim.task import WaitForTask

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
            return False # Do we want to check if this route works?

        # Return VM Name if match found
        if vm.name == search:
            return vm
    
    # Catch used if no matches were found
    else:
        print("VM not found, please try again") 
        return False # Default response if function is unable to locate vm

# Useful Resource: https://www.ntpro.nl/blog/archives/3751-Mastering-vCenter-Operations-with-Python-A-Script-to-Manage-Your-VMs.html
# Function used to power off a selected VM
def powerOffVM(si):
    # Query list of vms available to clone
    vm = selectVM(si)

    # Check if provided vm is valid
    if str(vm) == 'False':
        pass
    else:
        # Check to see if vm is already powered off
        if str(vm.runtime.powerState) == "poweredOff":
            print("VM already powered Off")
            pass
        # Powers off the selected vm
        else:
            vm.PowerOffVM_Task()
            print(vm.name+" has been powered off")


# Function used to power on a selected VM
def powerOnVM(si):
    # Query list of vms available to clone
    vm = selectVM(si)

    # Check if provided vm is valid
    if str(vm) == 'False':
        pass
    else:
        # Check to see if vm is already powered on
        if str(vm.runtime.powerState) == "poweredOn":
            print("VM already powered on")
            pass
        # Powers on the selected vm
        else:
            vm.PowerOnVM_Task()
            print(vm.name+" has been powered on")


# Function used to take a snapshot of a given VM
def takeVMSnapshot(si):
    # Query list of vms available to clone
    vm = selectVM(si)

    # Check if provided vm is valid
    if str(vm) == 'False':
        pass
    else:
        snapshotName = input("Please select a name for the new snapshot: ")
        
        # Catch if no name was provided
        if snapshotName == "":
            snapshotName = "snapshot"
            print("No snapshot name provided, defaulting to 'snapshot'")

        # User Confirmation
        print("")
        userConfirm = input("Are you sure you want to create the new '"+snapshotName+"' VM Snapshot? (y/n)")

        # Y/N Prompt
        loop = True
        while loop == True:
            if userConfirm == "y":
                # Action Item goes here
                vm.CreateSnapshot_Task(name=snapshotName, memory=False, quiesce=False)
                print("Snapshot created, task complete!")
                loop = False
            elif userConfirm == "n":
                print("stopping")
                loop = False
            # Catch for invalid inputs
            else:
                print("Invalid input, please try again")


# Function that reverts the VM to its latest working snapshot
def restoreVMSnapshot(si):
    # Query list of vms available to clone
    vm = selectVM(si)

    # Check if provided vm is valid
    if str(vm) == 'False':
        pass
    else:
        # User Confirmation
        print("")
        userConfirm = input("Are you sure you want to revert the VM to its latest Snapshot? (y/n)")

        # Y/N Prompt
        loop = True
        while loop == True:
            if userConfirm == "y":
                # Action Item goes here
                vm.RevertToCurrentSnapshot_Task()
                print("Snapshot successfully reverted!")
                loop = False
            elif userConfirm == "n":
                print("stopping")
                loop = False
            # Catch for invalid inputs
            else:
                print("Invalid input, please try again")


# Function used to modify memory for a given VM
# Source: https://github.com/vmware/pyvmomi-community-samples/blob/master/samples/create_vm.py
def modifyVMMem(si):
    # Query list of vms available to clone
    vm = selectVM(si)

    # Check if provided vm is valid
    if str(vm) == 'False':
        pass
    else:
        # User Confirmation
        print("")
        userConfirm = input("Are you sure you want modify the VM Memory Configuration? (y/n)")

        # Y/N Prompt
        loop = True
        while loop == True:
            if userConfirm == "y":
                # Powers off VM, Sets new memory config, Powers on VM
                vm.PowerOffVM_Task()
                newMem = input("Please input a new memory ammount (MB): ")
                task = vim.vm.ConfigSpec(memoryMB = int(newMem))
                WaitForTask(vm.Reconfigure(task))
                vm.PowerOnVM_Task()
                print("VM config has been updated!")
                loop = False
            elif userConfirm == "n":
                print("stopping")
                loop = False
            # Catch for invalid inputs
            else:
                print("Invalid input, please try again")


# Function used to remove a selected VM
def removeVM(si):
    # Query list of vms available to clone
    vm = selectVM(si)

    # Check if provided vm is valid
    if str(vm) == 'False':
        pass
    else:
        # User Confirmation
        print("")
        userConfirm = input("Are you sure you want delete the selected VM? (y/n)")

        # Y/N Prompt
        loop = True
        while loop == True:
            if userConfirm == "y":
                # Powers off and removes VM
                vm.PowerOffVM_Task()
                vm.Destroy_Task()
                print("VM sucessfully deleted")
                loop = False
            elif userConfirm == "n":
                print("stopping")
                loop = False
            # Catch for invalid inputs
            else:
                print("Invalid input, please try again")
    

def milestone5Menu(si):
    menuStatus = True
    while menuStatus == True:
        print("================================")
        print("Welcome to the VM Operation Menu!")
        print("")
        print("[1] - Power On VM")
        print("[2] - Power Off VM")
        print("[3] - Take VM Snapshot")
        print("[4] - Restore VM Snapshot")
        print("[5] - Configure VM Memory")
        print("[6] - Delete a VM")
        print("[7] - Exit to Main Menu")
        print("")
        selection = input("Please select an option from the menu above: ")

        if selection == "1":
            powerOnVM(si)
            continue

        if selection == "2":
            powerOffVM(si)
            continue
        
        if selection == "3":
            takeVMSnapshot(si)
            continue

        if selection == "4":
            restoreVMSnapshot(si)
            continue

        if selection == "5":
            modifyVMMem(si)
            continue

        if selection == "6":
            removeVM(si)
            continue

        if selection == "7":
            print("Exiting Script")
            menuStatus = False

        # Catch used to respond to unexpected inputs
        else:
            print("Invalid option, please try again")
            continue

