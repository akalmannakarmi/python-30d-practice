# Write a function generate_colors which can generate any number of hexa or rgb colors.

from random import choice,randint

def list_of_hexa_colors(n=1):
    values = '0123456789abcdef'
    result = []
    for i in range(n):
        t = '#'
        for i in range(6):
            t+=choice(values)
        result.append(t)
    return result

def list_of_rgb_colors(n=1):
    result = []
    for i in range(n):
        result.append((randint(0,255),randint(0,255),randint(0,255)))
    return result

def generate_colors(type,n=0):
    if type== "hexa":
        return list_of_hexa_colors(n)
    if type== "rgb":
        return list_of_rgb_colors(n)
    
print(generate_colors('hexa', 3)) # ['#a3e12f','#03ed55','#eb3d2b'] 
print(generate_colors('hexa', 1)) # ['#b334ef']
print(generate_colors('rgb', 3))  # ['rgb(5, 55, 175','rgb(50, 105, 100','rgb(15, 26, 80'] 
print(generate_colors('rgb', 1))  # ['rgb(33,79, 176)']