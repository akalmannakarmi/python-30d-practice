# Go to the data folder and access the countries-data.py file.
from data.countries_data import countries_data

# Create a function called the most_spoken_languages in the world. It should return 10 or 20 most spoken languages in the world in descending order
# Find the ten most spoken languages from the data
def most_spoken_languages(countries_data):
    result=[]
    languages = {}
    for country in countries_data:
        for language in country['languages']:
            if language not in languages:
                languages[language] = 1
            else:
                languages[language] +=1
                
    i=0
    for language in dict(sorted(languages.items(), key=lambda item: item[1], reverse=True)):
        if i>=10:
            break
        i+=1
        result.append(language)
    return result

# Create a function called the most_populated_countries. It should return 10 or 20 most populated countries in descending order.

def most_populated_countries(countries_data):
    result=[]
    country_population = {}
    for country in countries_data:
        country_population[country['name']]=country['population']
                
    i=0
    for country in dict(sorted(country_population.items(), key=lambda item: item[1], reverse=True)):
        if i>=10:
            break
        i+=1
        result.append(country)
    return result