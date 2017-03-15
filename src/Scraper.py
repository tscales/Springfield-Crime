import os.path
import time
import pandas as pd
from bs4 import BeautifulSoup
class scrapeData:
    def __init__(self):
        self.frames = []

    def scrape(self):
        '''initial method to capture data from springfieldCrimeAlert
        if the data exists locally it will not scrape again.'''

        if os.path.exists('data/Dataframe.pkl'):
            raise FileExistsError('Data already exists locally')

        self.url = 'https://www.springfieldcrimealert.com/crime_stats_'

        for year in range(2004,2017):
            page = self.url + str(year) + '.php'
            self.df = pd.read_html(self.page,header = 0, index_col = 0)
            self.df[0].index.name = None
            self.frames.append(self.df[0])
            time.sleep(2)
            
        self.df = pd.concat(self.frames,axis=1,keys=[year for year in range(2004,2017)])
        self.df.to_pickle('data/dataFrame.pkl')
