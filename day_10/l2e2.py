# Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.

eSum=0
oSum=0
for i in range(101):
    if i%2!=0:
        eSum+=i
    else:
        oSum+=i
    

print(f"The sum of all evens is {eSum}. And the sum of all odds is {oSum}.")