# Read the countries API and find
# the 10 largest countries
# the 10 most spoken languages
# the total number of languages in the countries API
# https://restcountries.eu/rest/v2/all
# server is down

# using https://restcountries.com/v2/all

import requests

response = requests.get("https://restcountries.com/v2/all")
datas = response.json()

def getArea(c):
    result = {}
    for data in datas:
        if 'name' not in data or 'area' not in data:
            continue
        result[data['name']] = data['area']
    result = sorted(result.items(),key=lambda item:item[1],reverse=True)
    return result[:c]

print(getArea(10))

def getLanguages(c):
    result = {}
    for data in datas:
        if 'languages' not in data:
            continue
        for lang in data['languages']:
            if lang['name'] in result:
                result[lang['name']] +=1
            else:
                result[lang['name']] =1
                
    result = sorted(result.items(),key=lambda item:item[1],reverse=True)
    return result[:c]

print(getLanguages(10))