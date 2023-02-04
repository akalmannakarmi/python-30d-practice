# Extract the table in this url (https://archive.ics.uci.edu/ml/datasets.php) and change it to a json file

import json
import requests
from bs4 import BeautifulSoup

url ="https://archive.ics.uci.edu/ml/datasets.php"

response = requests.get(url)
soup = BeautifulSoup(response.content,'html.parser')

tables = soup.find_all('table')
table = tables[0]
Tdata = []
for table in tables:
    for tr in table.find_all('tr'):
        t = []
        for td in tr.find_all('td'):
            t.append(str(td))
        Tdata.append(t)
        
with open("day_22/results/Tdata.json",'w',encoding='utf-8')as f:
    json.dump(Tdata,f,indent=4)