# Python program to check whether a list contains a sub list

def is_Sublist(l, s):                               # define class of is_Sublist which contains parameter of list=l & sublist=s
	sub_set = False
	if s == []:                         # If sublist is not contain any character
		sub_set = True
	elif s == l:
		sub_set = True
	elif len(s) > len(l):
		sub_set = False

	else:
		for i in range(len(l)):
			if l[i] == s[0]:
				n = 1
				while (n < len(s)) and (l[i+n] == s[n]):
					n += 1
				
				if n == len(s):
					sub_set = True

	return sub_set

a = [2,4,3,5,7]
b = [4,3]

print(is_Sublist(a, b))

