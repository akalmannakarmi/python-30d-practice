# Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:
age = input("Enter your age: ")
if age >= 18:
    print("You are old enough to learn to drive.")
else:
    print(f"You need {18-age} more years to learn to drive.")