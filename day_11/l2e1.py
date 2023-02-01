# Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.

def evens_and_odds(num):
    m = ''
    s=0
    for i in range(1,num+1,2):
        s+=1
    m+= f"The number of odds are {s}\n"
    s=0
    for i in range(0,num+1,2):
        s+=1
    m+= f"The number of evens are {s}"
    return m

print(evens_and_odds(100))
# The number of odds are 50.
# The number of evens are 51.