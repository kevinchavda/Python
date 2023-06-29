#Python program to remove an empty tuple(s) from a list of tuples(using filter method)

my_tuple=[(),('RAM','SHYAM','22','4'),('',),('1','TOPS','GOOD'),(),('NEAR','2','ABOUT')]


new_tuple= filter(None,my_tuple)            # If there is None in tuple in my_tuple then filter it.
print(type(new_tuple))
print(new_tuple)

for i in new_tuple:
    print(i)
