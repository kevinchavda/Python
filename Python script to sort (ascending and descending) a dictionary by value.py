# Python script to sort (ascending and descending) a dictionary by value.

import operator
d1={"Maths":1,"Physics":5,"Chemestry":3,"English":4,"Gujarati":2}
print("Original Dictionary: ",d1)

asc= dict(sorted(d1.items(),key=operator.itemgetter(1)))    # Sorted your dictionary into ascending 
print("Ascending: ",asc)

dsc= dict(sorted(d1.items(),key=operator.itemgetter(1), reverse=True))    # Sorted your dictionary into descending 
print("Descending: ",dsc)
