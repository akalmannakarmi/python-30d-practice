# Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list

from random import shuffle

def shuffle_list(myList):
    shuffle(myList)
    return myList

print(shuffle_list([1,2,3,4,5,6]))