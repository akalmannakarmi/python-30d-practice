# Go to the data folder and use the countries.py file. Loop through the countries and extract all the countries containing the word land.

from data.countries import countries

for country in countries:
    if country.find('land')!=-1:
        print(country)