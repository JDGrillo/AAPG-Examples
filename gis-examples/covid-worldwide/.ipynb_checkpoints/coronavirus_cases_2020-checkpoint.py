import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import requests
import re
from bs4 import BeautifulSoup

url = 'http://www.worldometers.info/coronavirus/'

header = {
  "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
  "X-Requested-With": "XMLHttpRequest"
}

r = requests.get(url, headers=header).text

r = re.sub(r'<.*?>', lambda g: g.group(0).upper(), r)

# soup = BeautifulSoup(r)

# html_source = re.sub(r'<.*?>', lambda g: g.group(0).upper(), html_source)

# print(soup.find('table', id="main_table_countries_today").findAll("tr"))

# table = soup.find('table', id="main_table_countries_today")

# rows = table.find_all("tr")
# for row in rows:
#     td = row.find_all("td")
#     for ele in td:
#         if ele.text == "" or ele.text.isspace():
#             ele.string = "0"
# print("table after is", table)

# print("soup is", soup.find_all("table")[0])

# print("r is", r)

data = pd.read_html(r)
print("data are", data)
# data = pd.read_html(str(soup.find('table', id="main_table_countries_today")))

# print("data are", data)

# data = pd.read_html('https://www.worldometers.info/coronavirus/')

# print("data are", data)

for data_cases in data:
    print(data_cases)
    
data_cases = data_cases[['Country,Other', 'TotalCases' ]]

world_data = gpd.read_file(r'/home/jd/AAPG-Examples/gis-examples/covid-worldwide/World_Map.shp')

plt.savefig("world.jpg")

world_data.plot()

for items in data_cases['Country,Other'].tolist():
    world_data_list = world_data['NAME'].tolist()
    if items in world_data_list:
        pass
    
world_data.replace('Korea, Republic of', 'S. Korea', inplace = True)
world_data.replace('Iran (Islamic Republic of)', 'Iran', inplace = True)
world_data.replace('United States', 'USA', inplace = True)
world_data.replace('United Kingdom', 'U.K.', inplace = True)
world_data.replace('United Arab Emirates', 'U.A.E.', inplace = True)
world_data.replace('Viet Nam', 'Vietnam', inplace = True)
world_data.replace('Macau', 'Macao', inplace = True)
world_data.replace('The former Yugoslav Republic of Macedonia', 'North Macedonia', inplace = True)
world_data.replace('Czech Republic', 'Czechia', inplace = True)
world_data.replace('Czech Republic', 'Czechia', inplace = True)
world_data.replace('Palestine', 'State of Palestine', inplace = True)

data_cases.rename(columns = {'Country,Other': 'NAME'}, inplace = True)

combined = world_data.merge(data_cases, on = 'NAME')

combined.to_file(r'/home/jd/AAPG-Examples/gis-examples/covid-worldwide/combined.shp')
