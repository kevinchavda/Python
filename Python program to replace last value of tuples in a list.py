# Python program to replace last value of tuples in a list.

l= [(1,2,3),(13,15,17),(100,200,300)]              # Create a list with using tuple

print([t[:-1] + (500,) for t in l])   # By using slicing we add 500 in place of from all tuple.
