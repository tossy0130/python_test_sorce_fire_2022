import datetime

import requests
from bs4 import BeautifulSoup, BeautifulStoneSoup

from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


to_date = datetime.datetime.now()
change_date = to_date.strftime("%Y-%m-%d")

print(change_date)

date_arr = [
    {'year': 2019, 'name': '令和', 'new_Japanese_calendar': '平成31年'},
    {'year': 1986, 'name': '平成', 'new_Japanese_calendar': '平成元年'},
    {'year': 1926, 'name': '昭和', 'new_Japanese_calendar': '大正15年'}
]

now_y = change_date[:4]
print(now_y)


def Gengou(now_y):
    for d_val in date_arr:
        if now_y == d_val['year']:
            print('333')
            print(d_val['new_Japanese_calendar'])
            # 年度の元年を返す
            return d_val['new_Japanese_calendar']

        if int(now_y) >= d_val['year']:
            year = int(now_y) - d_val['year'] + 1
            return d_val['name'] + str(year) + "年"


tem = Gengou(now_y)
print(tem)
