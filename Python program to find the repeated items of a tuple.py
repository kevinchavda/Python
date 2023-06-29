#Python program to find the repeated items of a tuple.


my_tuple=(1,2,3,4,5,6,1,2,3,23)             # Create a tuple 
my_list=[]                                  # Make a list 

for items in my_tuple:
    if my_tuple.count(items)>1:
        if items not in my_list:
            my_list.append(items)

print(my_list)
