import requests
from bs4 import BeautifulSoup


url = "http://www.jimnet.co.jp/"

r = requests.get(url)

soup = BeautifulSoup(r.content, 'html.parser')
# soup = BeautifulSoup(r.text, 'html.parser')

print(soup)
