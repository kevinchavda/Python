# Python program to get the largest number, smallest num and sum of all from a list.

# try block to handle the exception

my_list=int(input("Enter the elements:"))

try:
	my_list = []

	while True:
		my_list.append(int(input()))

# if the input is not-integer, just print the list
except:
	print(my_list)


my_list.sort()                       # Sorting mylist to asceding order
print(my_list)

total=sum(my_list)                   # Using sum() function addition of all elements in a list

print("Smallest Number: ",my_list[0])
print("Largest Number: ",my_list[-1])
print("Sum of all elements in a given list:",total)
