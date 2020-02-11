import pandas as pd
from selenium import webdriver
import requests
from bs4 import BeautifulSoup

# Pandas Settings
pd.options.display.max_columns = None
pd.options.display.max_rows = None

data_url = "https://www.ecdc.europa.eu/en/geographical-distribution-2019-ncov-cases"

data_page = requests.get(data_url)

soup = BeautifulSoup(data_page.text, "lxml")

table = soup.find("table", class_="table table-bordered table-condensed table-striped")
table_headers = table.find_all("th")
table_rows = table.tbody.find_all("tr")


headers = []

table_dict = {}

for th in table_headers:
    headers.append(th.text)

for h in headers:
    table_dict[h] = []

for tr in table_rows:
    for td, v in zip(tr.find_all("td"), table_dict.values()):
        try:
            v.append(td.text)
        except:
            v.append("NaN")

corona_data_df = pd.DataFrame.from_dict(table_dict)
corona_data_df = corona_data_df[:-1]
print(corona_data_df)
