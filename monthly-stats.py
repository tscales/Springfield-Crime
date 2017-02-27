import json
import requests
import time
from bs4 import BeautifulSoup

data = {}
page = 'https://www.springfieldcrimealert.com/crime_stats_'
for year in range(2004,2017):
    data[str(year)] = {}
    r = requests.get(page + str(year) + '.php')
    soup = BeautifulSoup(r.text,'html.parser')
    table = soup.table
    rows = table.find_all('tr')
    for row in rows[1:]:
        cols = [cell.text.strip().lower() for cell in row.find_all('td')]
        incident = cols[0]
        amounts = [float(i) for i in cols[1:]]
        data[str(year)][incident] = amounts
    time.sleep(2)

with open('text7.txt','w') as f:
    json.dump(data,f)
    
print('complete')
    
