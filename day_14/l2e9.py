# Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.

def get_string_lists(myList):
    return list(map(str,myList))

print(get_string_lists([12312,123.123,"12312",(12,34)]))