import requests
from bs4 import BeautifulSoup as bs

URL = "https://quotes.toscrape.com/"

response = requests.get(URL)
soup = bs(response.text, features='lxml')
quotes = soup.find_all('span', class_='text')
author = soup.find_all('small', class_='author')

for i in range(0, len(quotes)):
    print(f'{quotes[i].text} \n--{author[i].text}\n')
