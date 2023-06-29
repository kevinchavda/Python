# Write a Python program to check multiple keys exists in a dictionary

d={1:1000,2:2000,3:3000,4:4000}    # Make a dictionary

user_input=int(input("Give some reference ID: ")) # Get a referance input from user

if user_input in d:
    print("The key is exist")

else:
    print("The key is not exist")
