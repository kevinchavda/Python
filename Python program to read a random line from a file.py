#Python program to read a random line from a file.

import random

def ReadRandomLine():                  # Define a function
    f=open("file1.txt","r")            # Open your file in read mode
    lines=f.readlines()                # Reaad lines from file
    #print(lines)                       # Print all lines
    
    r1=random.randint(0,len(lines)-1)  # Using randint function pick a random value from a list of lines
    print(lines[r1])                   # Print lines of r1
    f.close()
    
ReadRandomLine()
    

