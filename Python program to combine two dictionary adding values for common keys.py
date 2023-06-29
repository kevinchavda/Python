#Python program to combine two dictionary adding values for common keys.

d1 = {'a': 100, 'b': 200, 'c':300}   # Here d1 & d2 dictionaries have some common keys 
d2 = {'a': 300, 'b': 200, 'd':400}


for key in d1.keys():
    if key in d2.keys():         # If key is match in both dictionary than addition of their value.
        d1[key]=d1[key]+d2[key]  

    d2[key]=d1[key]

print(d2)
