# The best solution 
# Searching - find address for files  *.py
import os

for cur_dir, subdirs, files in os.walk("main"): # name root folder for search 
    for file in files:
        if file.endswith(".py"): # key search parameter 
            print(cur_dir)
            break