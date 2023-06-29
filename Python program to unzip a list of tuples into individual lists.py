# Python program to unzip a list of tuples into individual lists

my_list=[(10,23,45),('JD','RUN','HELP'),(100,200,300)]   # Make a list of tuple 
print(list(zip(*my_list)))# Using zip(*) function unzip your list fo tuples into individual lists 
