<<<<<<< HEAD
from bs4 import BeautifulSoup
import requests
from tabulate import tabulate

url = 'http://www.twse.com.tw/ch/trading/indices/twco/tai50i.php'

r = requests.get(url)
r.encoding = "big5"
soup = BeautifulSoup(r.text, "lxml")
items = soup.findAll("tr", {'class': "tb2"})
headers = ["代號", "名稱", "產業類別細分", "發行股數(單位:股)", "公眾流通量係數", "占臺灣50指數權重"]
table = []
for i in range(len(items)):
    tds = items[i].findAll("td")
    td1 = tds[0].text
    td2 = tds[1].text
    td3 = tds[2].text
    td4 = tds[3].text
    td5 = tds[4].text
    td6 = tds[5].text
    td = [td1, td2, td3, td4, td5, td6]
    table.append(td)
print(tabulate(table, headers=headers, tablefmt="rst", numalign="right"))
=======
from bs4 import BeautifulSoup
import requests
from tabulate import tabulate

url = 'http://www.twse.com.tw/ch/trading/indices/twco/tai50i.php'

r = requests.get(url)
r.encoding = "big5"
soup = BeautifulSoup(r.text, "lxml")
items = soup.findAll("tr", {'class': "tb2"})
headers = ["代號", "名稱", "產業類別細分", "發行股數(單位:股)", "公眾流通量係數", "占臺灣50指數權重"]
table = []
for i in range(len(items)):
    tds = items[i].findAll("td")
    td1 = tds[0].text
    td2 = tds[1].text
    td3 = tds[2].text
    td4 = tds[3].text
    td5 = tds[4].text
    td6 = tds[5].text
    td = [td1, td2, td3, td4, td5, td6]
    table.append(td)
print(tabulate(table, headers=headers, tablefmt="rst", numalign="right"))
>>>>>>> 29268a447a108c51b89818ca636050cdee8e24f9
