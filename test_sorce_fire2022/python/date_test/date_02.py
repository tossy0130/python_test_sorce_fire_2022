import datetime

import requests
from bs4 import BeautifulSoup, BeautifulStoneSoup

from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class Gengou():

    def __init__(self):
        pass

    def Data_Set(self):
        date_arr = [
            {'year': 2019, 'name': '令和', 'new_Japanese_calendar': '平成31年'},
            {'year': 1986, 'name': '平成', 'new_Japanese_calendar': '平成元年'},
            {'year': 1926, 'name': '昭和', 'new_Japanese_calendar': '大正15年'}
        ]
        return date_arr

    def Gengou_Print(self, now_y, r_month, date_arr):
        for d_val in date_arr:
            if now_y == d_val['year']:

                if r_month < 5:
                    # 年度の元年を返す
                    return d_val['new_Japanese_calendar']
                else:
                    return '令和元年'

            if int(now_y) >= d_val['year']:
                year = int(now_y) - d_val['year'] + 1
                return d_val['name'] + str(year) + "年"


# 出力
to_date = datetime.datetime.now()
change_date = to_date.strftime("%Y-%m-%d")


now_y = change_date[:4]  # 西暦 取得
month = change_date[5:7]  # 月　取得


Genotu_obj = Gengou()
data_set = Genotu_obj.Data_Set()
gengou_y = Genotu_obj.Gengou_Print(now_y, month, data_set,)
print(gengou_y)
