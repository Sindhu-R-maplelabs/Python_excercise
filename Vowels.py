
from itertools import permutations
chars_list=('a','e','i','o','u')
allStrigs =permutations(chars_list)
for string in allStrigs:
    print(''.join(string))
