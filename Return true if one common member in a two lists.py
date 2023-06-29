#Python program that takes two lists and returns true if they have at least one common member.

def com_data(list1, list2):
    result =False

    for x in list1:
        for y in list2:
            if x==y:
                result=True
                return result
    return result

# take a list from user

a= [x for x in input("Enter a list 1:").split()]
b= [x for x in input("Enter a list 2:").split()]
print(com_data(a,b))
