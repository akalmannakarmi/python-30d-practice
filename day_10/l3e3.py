#### Go to the data folder and use the countries_data.py file.
from data.countries_data import countries_data

# What are the total number of languages in the data
languages = []
for country in countries_data:
    for language in country['languages']:
        if language not in languages:
            languages.append(language)

print(f"No of languages: {len(languages)}")

# Find the ten most spoken languages from the data
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
    print(language,languages[language])

# Find the 10 most populated countries in the world
country_population = {}
for country in countries_data:
    country_population[country['name']]=country['population']
            
i=0
for country in dict(sorted(country_population.items(), key=lambda item: item[1], reverse=True)):
    if i>=10:
        break
    i+=1
    print(country,country_population[country])