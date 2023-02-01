# Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.

def sum_of_odds(num):
    s=0
    for i in range(1,num,2):
        s+=i
    return s