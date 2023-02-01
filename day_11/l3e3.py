# Write a function which checks if all the items of the list are of the same data type.
    
def same_datatype(list):
    type1 = type(list[0])
    for item in list:
        if type(item)!=type1:
            return False
    return True