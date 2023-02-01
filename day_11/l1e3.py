# Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.

def add_all_nums(*nums):
    sum = 0
    for num in nums:
        if type(num) not in (float,int):
            print(f"{num} is not a number")
            continue
        sum += num
    return sum