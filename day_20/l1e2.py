# Read the cats API and cats_api = 'https://api.thecatapi.com/v1/breeds' and find :
# the min, max, mean, median, standard deviation of cats' weight in metric units.
# the min, max, mean, median, standard deviation of cats' lifespan in years.
# Create a frequency table of country and breed of cats

import requests
import statistics

response = requests.get("https://api.thecatapi.com/v1/breeds")
datas = response.json()

def getWeights():
    weights=[]
    for data in datas:
        w = data['weight']['metric']
        s,b = w.split('-')
        w = (float(s) + float(b))/2
        weights.append(w)
    return weights
def getLifespan():
    lifespans=[]
    for data in datas:
        l = data['life_span']
        s,b = l.split('-')
        l = (float(s) + float(b))/2
        lifespans.append(l)
    return lifespans

weights = getWeights()
print("By Weight")
print(f"Min weight:{min(weights)}")
print(f"Max weight:{max(weights)}")
print(f"Mean weight:{statistics.mean(weights)}")
print(f"Median weight:{statistics.median(weights)}")
print(f"STD weight:{statistics.stdev(weights)}")
lifespans = getLifespan()
print("By Lifespan")
print(f"Min lifespan:{min(lifespans)}")
print(f"Max lifespan:{max(lifespans)}")
print(f"Mean lifespan:{statistics.mean(lifespans)}")
print(f"Median lifespan:{statistics.median(lifespans)}")
print(f"STD lifespan:{statistics.stdev(lifespans)}")

def getfrequency():
    table={}
    for data in datas:
        k = (data['name'],data['origin'])
        if k in table:
            table[k] +=1
        else:
            table[k] = 1
    return table

def displayTable():
    print("Breed \tCountry \tFrequency".expandtabs(24))
    for k,f in getfrequency().items():
        print(f"{k[0]}\t{k[1]}\t{f}".expandtabs(24))

displayTable()
