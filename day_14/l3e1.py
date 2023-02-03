# Use the countries_data.py (https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries-data.py) file and follow the tasks below:
from data.countries_data import countries_data

# Sort countries by name, by capital, by population
countries_data.sort(key=lambda c : c['name'])
# print(countries_data)
countries_data.sort(key=lambda c : c['capital'])
# print(countries_data)
countries_data.sort(key=lambda c : c['population'])
# print(countries_data)


# Sort out the ten most spoken languages by location.

languages={}
for country in countries_data:
    for language in country['languages']:
        if language in languages:
           languages[language] +=1
        else:
            languages[language] = 1
# print(languages)

# Sort out the ten most populated countries.


countries_data.sort(key=lambda c : c['population'],reverse=True)
for i,country in enumerate(countries_data):
    if i>=10:
        break
    print(f"{country['name']}:{country['population']}")

