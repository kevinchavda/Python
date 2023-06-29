#Python program to calculate the area of a trapezoid

# area of trapazoid = ((base_1 + base_2) / 2) * height

height= float(input("Give value of Height: "))      # Get value from user
base_1= float(input("Give value of base 1: "))
base_2= float(input("Give value of base 2: "))

area= ((base_1 + base_2) / 2) * height

print("Area of Trapazoid: ",area)
