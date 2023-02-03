# Read the countries_data.json data file in data directory, create a function that creates a list of the ten most populated countries

import json

def most_populated_countries(file,count):
    with open("day_19/data/"+file,encoding='utf-8') as f:
        countries_data=json.load(f)
    result=[]
    country_population = {}
    for country in countries_data:
        country_population[country['name']]=country['population']
                
    country_population=sorted(country_population.items(), key=lambda item: item[1], reverse=True)
    return country_population[:count]

# Your output should look like this
print(most_populated_countries('countries_data.json', 10))

[
{'country': 'China', 'population': 1377422166},
{'country': 'India', 'population': 1295210000},
{'country': 'United States of America', 'population': 323947000},
{'country': 'Indonesia', 'population': 258705000},
{'country': 'Brazil', 'population': 206135893},
{'country': 'Pakistan', 'population': 194125062},
{'country': 'Nigeria', 'population': 186988000},
{'country': 'Bangladesh', 'population': 161006790},
{'country': 'Russian Federation', 'population': 146599183},
{'country': 'Japan', 'population': 126960000}
]

# Your output should look like this

print(most_populated_countries('countries_data.json', 3))
[
{'country': 'China', 'population': 1377422166},
{'country': 'India', 'population': 1295210000},
{'country': 'United States of America', 'population': 323947000}
]