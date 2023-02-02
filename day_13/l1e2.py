# Flatten the following list of lists of lists to a one dimensional list :

list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

# output
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

list_of_lists = [i for row in list_of_lists for r in row for i in r]
print(list_of_lists)