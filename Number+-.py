#Write a Python program to check if a number is positive, negative or zero.
n=int(input("Enter Number : "))
if n>=0:
    if n==0:
        print("It is Zero")
    else:
        print("Number is Positive.")
else:
    print("Number is Negative")
