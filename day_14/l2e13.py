# Create a function returning a dictionary, where keys stand for starting letters of countries and values are the number of country names starting with that letter.
from data.countries import countries

result={}
def startsWith(name):
    if name[0] in result:
        result[name[0]] +=1
    else:
        result[name[0]] = 1

list(filter(startsWith,countries))
print(result)