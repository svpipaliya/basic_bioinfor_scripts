#!/usr/bin/env python
## This script reads and removes a single specified special character from a string
## Ask Shweta if you are confused

#Replace a set of multiple sub strings with a new string in main string.

mainStr = "Hello, This is a sample string"
def replaceMultiple(mainString, toBeReplaces, newString):
    # Iterate over the strings to be replaced
    for elem in toBeReplaces :
        # Check if string is in the main string
        if elem in mainString :
            # Replace the string
            mainString = mainString.replace(elem, newString)
    
    return  mainString     
 
def main():
    
    mainStr = "Hello, This is a sample string"
 # Replace all occurrences of given character or string in main string
    otherStr = mainStr.replace('s' , 'X') 
     
    print("String with replaced Content : " , otherStr) 
    
    #Replace First 2 occurrences of given character or string in main string
    otherStr = mainStr.replace('s' , 'XXXS', 2) 
     
    print(otherStr) 
    
    
#Replace multiple characters / strings from a string
  
    # Replace all the occurrences of string in list by AA in the main list 
    otherStr = replaceMultiple(mainStr, ['s', 'l', 'a'] , "AA")
    
    print(otherStr)
           
if __name__ == '__main__':
    main()
    
##End