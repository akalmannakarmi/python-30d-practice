# Use map to create a new list by changing each country to uppercase in the countries list

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']

def toUpper(s):
    return s.upper()

U_countries=map(toUpper,countries)
print(list(U_countries))