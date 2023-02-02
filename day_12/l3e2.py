# Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.

from random import randint

def randNums():
    result = []
    while len(result)<7:
        v = randint(0,9)
        if v in result:
            continue
        result.append(v)
    return result

print(randNums())