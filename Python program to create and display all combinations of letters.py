"""
Python3 code to demonstrate working of Dictionary key combinations
Using itertools.combinations()
"""

import itertools

# Initializing dict
d= {'1': ['a','b'], '2': ['c','d']}

for combo in itertools.product(*[d[k] for k in sorted(d.keys())]):
    print(''.join(combo))



