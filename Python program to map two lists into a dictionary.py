# Write a Python program to map two lists into a dictionary(By using zip function)

name=["Jaydeep","Milan","Shivam","Dhruti"]    # Make a lists 
marks=[89,76,78,80]

dictionary=zip(name,marks)   # Using Zip() function we create a tuple
print(dict(dictionary))   # By using dict()function we convert tuple into a dictionary
