# Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
x=0
while True:
    y = x**2 + 6*x + 9
    if(y==0):
        print(f"When x is {x}")
        break
    x-=1