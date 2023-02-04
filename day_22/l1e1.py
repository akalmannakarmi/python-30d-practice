# Scrape the following website and store the data as json file(url = 'http://www.bu.edu/president/boston-university-facts-stats/').

import requests
import json
from bs4 import BeautifulSoup

url = 'http://www.bu.edu/president/boston-university-facts-stats/'

response = requests.get(url)
content = response.content
soup = BeautifulSoup(content,'html.parser')
with open("day_22/results/data.json",'w',encoding='utf-8')as f:
    json.dump(str(soup.body),f)