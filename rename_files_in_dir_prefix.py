#!/usr/bin/env python 

# Python program to rename all filenames with specific prefix in your directory  
import os 
  
os.chdir('D://Geeksforgeeks') 
print(os.getcwd()) 
COUNT = 1
  
# Function to increment count  
# to make the files sorted. 
def increment(): 
    global COUNT 
    COUNT = COUNT + 1
  
  
for f in os.listdir(): 
    f_name, f_ext = os.path.splitext(f) 
    f_name = "geek" + str(COUNT) 
    increment() 
  
    new_name = '{} {}'.format(f_name, f_ext) 
    os.rename(f, new_name)
    
#end