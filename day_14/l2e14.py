# Declare a get_first_ten_countries function - it returns a list of first ten countries from the countries.js list in the data folder.

from data.countries import countries

def get_first_ten_countries():
    return countries[:10]

print(get_first_ten_countries())