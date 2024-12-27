import requests
import html5lib
from bs4 import BeautifulSoup
import csv

base_url = "https://losangeles.craigslist.org/search/rea#search=1~gallery~0~0"
response = requests.get(base_url)
soup = BeautifulSoup(response.content, "html5lib")

ol = soup.find("ol", attrs={"class":"cl-static-search-results"})
list_ = ol.findAll("li", attrs={"class":"cl-static-search-result"})

real_estate_data = []

for items in list_:
    title = items.find("div", attrs={"class":"title"})
    details = items.find("div", attrs={"class":"details"})
    price = details.find("div", attrs={"class":"price"})
    location = details.find("div", attrs={"class":"location"})
    real_estate_data.append(
        {"Title": title.text.strip(),
         "Price": price.text.strip(),
         "Location": location.text.strip()
         }
    )


with open("LA_real_estate.csv", mode="w", newline='',encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=["Title", "Price", "Location"])
    writer.writeheader()

    for row in real_estate_data:
        writer.writerow(row)