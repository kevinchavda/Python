# Python program to calculate surface volume and area of a cylinder
"""
volume of cylinder = pi * radius * radius * height
surface area of culinder = ((2*pi*radius) * height) + ((pi*radius**2)*2)
"""
pi=22/7                                         # Define value of pi
radius=float(input("Give value of radius: "))   # Take input from user
height=float(input("Give value of height: "))

volume= pi * radius * radius * height
surface_area = ((2*pi*radius) * height) + ((pi*radius**2)*2)

print("Volume of Cylinder : ",volume)
print("Surface area of Cylinder : ",surface_area)
