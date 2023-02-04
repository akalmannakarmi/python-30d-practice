# Scrape the presidents table and store the data as json(https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States). The table is not very structured and the scrapping may take very long time.

import json
import requests
from bs4 import BeautifulSoup

url ="https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States"

response = requests.get(url)
soup = BeautifulSoup(response.content,'html.parser')

table = soup.find('table',{'class':"wikitable sortable"})
Tdata = []

for tr in table.find_all('tr'):
    t = []
    for td in tr.find_all('td'):
        t.append(str(td))
    Tdata.append(t)
        
with open("day_22/results/presidentsData.json",'w',encoding='utf-8')as f:
    json.dump(Tdata,f,indent=4)