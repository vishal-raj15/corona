import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import numpy as np
url = "https://www.worldometers.info/coronavirus/"

r = requests.get(url)
html = r.text
soup = BeautifulSoup(html ,'html.parser')
print(soup.title)

table_body = soup.find('tbody')
table_row = table_body.find_all('tr')

countries=[]
cases = []
todays = []
deaths =[]
death=[]
x=[]

for tr in table_row:
    id = tr.find_all('td')
    countries.append(id[0].text)
    cases.append(id[1].text)
    todays.append(id[2].text)
    death.append(id[3].text)
sum1 = 0 
for i in range(len(death)):
    if(death[i] == ' '):
        a = 0
    else:
        a = int(death[i].replace(',' ,''))
    deaths.append(a)
    x.append(i)
    sum1 += deaths[i]
    
print("total deaths today :",sum1)
<<<<<<< HEAD
#plt.plot(x , deaths)
#plt.show()
=======
plt.plot(x , deaths)
plt.show()
>>>>>>> 771979ea39fb36271387d645ea1578e48fac476f
