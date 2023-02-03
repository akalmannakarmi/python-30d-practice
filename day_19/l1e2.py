# Read the countries_data.json data file in data directory, create a function that finds the ten most spoken languages

import json

def most_spoken_languages(file,count):
    with open("day_19/data/"+file,encoding='utf-8') as f:
        countries_data=json.load(f)
    languages = {}
    for country in countries_data:
        for language in country['languages']:
            if language not in languages:
                languages[language] = 1
            else:
                languages[language] +=1
    languages = sorted(languages.items(), key=lambda item: item[1], reverse=True)
    return languages[:count]

# Your output should look like this
print(most_spoken_languages('countries_data.json', 10))
[(91, 'English'),
(45, 'French'),
(25, 'Arabic'),
(24, 'Spanish'),
(9, 'Russian'),
(9, 'Portuguese'),
(8, 'Dutch'),
(7, 'German'),
(5, 'Chinese'),
(4, 'Swahili'),
(4, 'Serbian')]

# Your output should look like this
print(most_spoken_languages('countries_data.json', 3))
[(91, 'English'),
(45, 'French'),
(25, 'Arabic')]