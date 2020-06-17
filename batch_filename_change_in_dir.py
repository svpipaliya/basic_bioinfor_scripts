#!/usr/local/bin/python
# batch filename change in directory
import os
import shutil
from os import path

def main():
	# make a duplicate of an existing file
    if path.exists("filename.txt"):
	# get the path to the file in the current directory
        src = path.realpath("filename.txt");
		
	# rename the original file
        os.rename('filename.txt','newfilename.txt') 
		
if __name__ == "__main__":
    main()
    
#end