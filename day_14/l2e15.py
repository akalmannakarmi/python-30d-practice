# Declare a get_last_ten_countries function that returns the last ten countries in the countries list.

from data.countries import countries

def get_last_ten_countries():
    return countries[-10:]

print(get_last_ten_countries())