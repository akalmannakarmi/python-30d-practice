# Filter only negative and zero in the list using list comprehension

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]

numbers = [i for i in numbers if i>1]
print(numbers)