import json
import requests
import time
from bs4 import BeautifulSoup


class Crime_scraper:
    def __init__(self):
        with open('data/police-reports-data-set.txt','r') as f:
            self.data = json.load(f)
        
        self.main_url = 'https://www.springfieldcrimealert.com/reports.php?p='
        self.address_url = 'https://www.springfieldcrimealert.com/addr/'
        self.page_num = 1
        self.report_nums = [i['report-num'] for i in self.data['data']]
        self.new_latest_report = None

    def get_main_page(self):
        '''gets most recent reports table'''
        r = requests.get(self.main_url + str(self.page_num))
        return BeautifulSoup(r.text,'html.parser')

    def get_address_reports(self, address):
        '''get the report for each item on the most recent
        reports table'''
        print('collecting reports for: ' + address)
        fixed_address= address.replace('&','and')
        fixed_address= fixed_address.replace(' ','_')
        r = requests.get(self.address_url + fixed_address + '.htm')
        soup = BeautifulSoup(r.text,'html.parser')
        table = soup.table
        if table is None:
            print('no table here boss!')
            return 
        rows = table.find_all('tr')[1:]
        for row in rows:
            cols = row.find_all('td')
            cols = [cell.text.strip() for cell in cols]
            if cols[1] in self.report_nums:
                continue
            if len(cols) == 3:
                self.data['data'].append({'data':cols[0],'report-num':cols[1],
                                          'incident':cols[2],'location':address})
        

    def get_new_reports(self):
        '''for each item on the new reports table, check if there are more reports
        from that address not in the dataset and add them to it'''
        running = True
        print('scraping page: ' + str(self.page_num))
        main_page = self.get_main_page()
        table = main_page.table
        rows = table.find_all('tr')[1:]
        if self.page_num == 1:
            self.new_latest_report = rows[0].find_all('td')[0].text.strip()
        for row in rows:
            cols = row.find_all('td')
            cols = [cell.text.strip() for cell in cols]
            if cols[0]== self.data['latest']:
                self.data['latest'] = self.new_latest_report
                with open('data/police-reports-data-set.txt','w') as f:
                    json.dump(self.data,f)
                running = False
                break
            if len(cols) > 1:
                self.data['data'].append({'report-num':cols[0],'date':cols[1],
                                     'incident':cols[2],'location':cols[3]})
                self.get_address_reports(cols[3])
                time.sleep(2.5)
    
        if running:
            self.page_num+= 1
            print('scraping page: ' + str(self.page_num))
            self.get_new_reports()

test= Crime_scraper()
test.get_new_reports()
print('complete')
