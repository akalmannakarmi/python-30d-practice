# Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:
a = int(input("Enter a: "))
b = int(input("Enter b: "))
if a>b:
    print("a is greater than b")
elif b>a:
    print("b is greater than a")
else:
    print("a is equal to b")