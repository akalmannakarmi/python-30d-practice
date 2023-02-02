# Write a function list_of_rgb_colors which returns any number of RGB colors in an array.

from random import randint

def list_of_rgb_colors(n=1):
    result = []
    for i in range(n):
        result.append((randint(0,255),randint(0,255),randint(0,255)))
    return result

print(list_of_rgb_colors(10))