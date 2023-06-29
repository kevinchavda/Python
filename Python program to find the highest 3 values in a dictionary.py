# Python program to find the highest 3 values in a dictionary

fruits={"mango": 30,"Papaya": 50, "Strawberry": 40,"Banana": 35,"Apple": 100} # Take a dictionary

costly_fruit= sorted(fruits,key=fruits.get,reverse=True)   # Sorted this dictionary & save it to another variable

for index in range(3):
    print(costly_fruit[index])
