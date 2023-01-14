# Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:
my_Age = int(input("Enter my age: "))
your_Age = int(input("Enter your age: "))
if my_Age>your_Age:
    diff = my_Age-your_Age
    if diff == 1:
        print(f"I am {diff} year older than you")
    else:
        print(f"I am {diff} years older than you")
elif my_Age<your_Age:
    diff = your_Age-my_Age
    if diff == 1:
        print(f"You are {diff} year older than me")
    else:
        print(f"You are {diff} years older than me")
else:
    print(f"We have same age")