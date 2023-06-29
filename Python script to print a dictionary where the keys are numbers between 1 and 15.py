#Python script to print a dictionary where the keys are numbers between 1 and 15(using for loop).

dict= {}
n=15  # According to question

"""
But if you want to take user input then write
n=int(input("Give range:"))
"""
    
for x in range(1,n+1):     # use of for loop.
    dict[x]=x*x

print(dict)


