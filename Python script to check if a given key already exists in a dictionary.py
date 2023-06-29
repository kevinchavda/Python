# Python script to check if a given key already exists in a dictionary.

d= {1: 100, 2: 200, 3: 300, 4: 400, 5: 500, 6: 600}   # Create a dictionary

def key_presence(x):

    if x in d:
        print("Key is present in dictionary")
        
    else:
        print("Key is not present in dictionary")

# Call a function
x=int(input("Give a key referance: "))
print(key_presence(x))
