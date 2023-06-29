#Python function to check whether a number is perfect or not
"""
    According to maths rule a perfect number is a positive integer that is equal to the sum
    of its proper positive divisors,that is, the sum of its positive divisors
    excluding the number itself
"""

def test_number(n):

    sum=0
    for x in range(1,n):
        if n%x==0:
            sum=sum+x
    return sum==n
print(test_number(6))
