import json
import requests
import time
from bs4 import BeautifulSoup
data = {}
for year in range(2004,2017):
    data[str(year)] ={
                      'jan':{},
                      'feb':{},
                      'mar':{},
                      'apr':{},
                      'may':{},
                      'jun':{},
                      'jul':{},
                      'aug':{},
                      'sep':{},
                      'oct':{},
                      'nov':{},
                      'dec':{}
                      }


    page= 'https://www.springfieldcrimealert.com/crime_stats_'+str(year)+'.php'
    r = requests.get(page)
    soup = BeautifulSoup(r.text,'html.parser')
    table = soup.table
    rows = table.find_all('tr')[1:]

    for row in rows:
        cols = [cell.text.strip().lower() for cell in row.find_all('td')]
        incident = cols[0]
        data[str(year)]['jan'][incident] = cols[1]
        data[str(year)]['feb'][incident] = cols[2]
        data[str(year)]['mar'][incident] = cols[3]
        data[str(year)]['apr'][incident] = cols[4]
        data[str(year)]['may'][incident] = cols[5]
        data[str(year)]['jun'][incident] = cols[6]
        data[str(year)]['jul'][incident] = cols[7]
        data[str(year)]['aug'][incident] = cols[8]
        data[str(year)]['sep'][incident] = cols[9]
        data[str(year)]['oct'][incident] = cols[10]
        data[str(year)]['nov'][incident] = cols[11]
        data[str(year)]['dec'][incident] = cols[12]
    time.sleep(2)
with open('year-stats-3.txt','w') as f:
    json.dump(data,f)
print('complete')

    