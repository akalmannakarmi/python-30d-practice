# Write a functions which checks if all items are unique in the list.

def unique(list):
    for item in list:
        if list.count(item) >1:
            return False
    return True