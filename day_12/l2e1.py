# Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).

from random import choice

def list_of_hexa_colors(n=1):
    values = '0123456789abcdef'
    result = []
    for i in range(n):
        t = '#'
        for i in range(6):
            t+=choice(values)
        result.append(t)
    return result

print(list_of_hexa_colors(10))