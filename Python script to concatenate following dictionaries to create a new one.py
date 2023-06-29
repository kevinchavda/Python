#Python script to concatenate following dictionaries to create a new one

# Take a sample dictionaries

dic1={1:100,2:200,3:300}
print("Dictionary 1: ",dic1)

dic2={4:400,5:500}
print("Dictionary 2: ",dic2)

dic3={6:600}
print("Dictionary 3: ",dic3)

dic4={} # Concatenate all these three dictionaries and save it to dic4 variable

for d in (dic1,dic2,dic3):
    dic4.update(d)

print("Updated Dictionary: ",dic4)
