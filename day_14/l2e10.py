# Use reduce to sum all the numbers in the numbers list.
from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def sum(a,b):
    return a+b

sumAll = reduce(sum,numbers)
print(sumAll)