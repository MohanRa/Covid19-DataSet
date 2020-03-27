from bs4 import BeautifulSoup
import requests as req    
import pandas as pd
import os
from datetime import date

today = date.today()
filename='<Folder Path>\Covid19_{}.csv'.format(today)
contents = req.get("https://www.worldometers.info/coronavirus/")
res=[]
soup = BeautifulSoup(contents.text, 'lxml')
table = soup.find_all('table')[1]
table_rows = table.find_all('tr')
data_row=pd.DataFrame()
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text for i in td]
    if(len(row)>0):
        res.append(row) 
Corona_26_3=pd.DataFrame(res,columns=['Country','Total cases','New Cases','Total Deaths','New Deaths','Total Recovered','Active cases','Serious,Critical','Tot cases 1M pop','Tot Death 1M pop'])
if not os.path.isfile(filename):
    Corona_26_3.to_csv(filename, header='column_names', encoding='utf-8')
else:
    Corona_26_3.to_csv(filename, mode='a', header=False, encoding='utf-8')