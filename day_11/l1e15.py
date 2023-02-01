# Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.

def sum_of_even(num):
    s=0
    for i in range(0,num,2):
        s+=i
    return s