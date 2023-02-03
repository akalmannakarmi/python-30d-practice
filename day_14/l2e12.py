# Declare a function called categorize_countries that returns a list of countries with some common pattern (you can find the countries list in this repository as countries.js(eg 'land', 'ia', 'island', 'stan')).
from data.countries import countries

def lands(name):
    if name.find('land') != -1:
        return True

def categorize_countries():
    return list(filter(lands,countries))

print(categorize_countries())