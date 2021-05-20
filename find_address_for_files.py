# Searching - find address for files  *.py
import os
folder = []
addres = []
for i in os.walk('main'): # name root folder for search 
    folder.append(i)
for address, dirs, files in folder:
    for file in files:
        if file[-3:] == '.py': # key search parameter 
            if address not in addres:
                addres.append(address)
print('\n'.join(addres))