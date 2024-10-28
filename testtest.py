# Function used to gather all availabe VMs found on host + filters

"""
Params:
    - VM_Name (optional)

"""

def showVM(VM_Name=None):
  
  # Checks to see if default value is set
  if VM_Name == None:
    print("Default value here")
  
  # If not, runs the search against the available list
  else:
    print(VM_Name)



### Testing
showVM("bruh")
print('======')
print("Var Testing below:")
showVM()