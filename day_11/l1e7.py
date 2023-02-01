# Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.

def solve_quadratic_eqn(a,b,c):
    return (-b+(b**2 -4*a*c)**.5)/(2*a)