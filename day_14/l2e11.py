# Use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries
from functools import reduce

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']

def make(*args):
    return ", ".join(args[0][: -1])  + f" and {args[0][-1]} are north European countries"

print(make(countries))