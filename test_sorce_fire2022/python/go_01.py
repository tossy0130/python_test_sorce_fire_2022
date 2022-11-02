import requests
from bs4 import BeautifulSoup, BeautifulStoneSoup

from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# === スクレイピング 01 クラス


class Scraping_Soup_01():

    def __init__(self, set_url, set_parse):
        self.url = set_url  # 対象 URL
        self.parse_op = set_parse  # パースオプション

    def Print_Soup(self):
        response = requests.get(self.url, verify=False)
        html_text = BeautifulSoup(response.text, self.parse_op)
        print(html_text)


scr_obj = Scraping_Soup_01('https://192.168.254.204/kdemo/index.php', 'lxml')
scr_obj.Print_Soup()


class Selenium_Test():

    driver = webdriver.Chrome(
        executable_path=r'C:\\chromedriver_win32\\chromedriver.exe')

    # カレントの URL 取得
    def Current_url(self, url):
        print(url)
        print('カレントURL:::' + self.driver.current_url)


Sel_obj = Selenium_Test()
Sel_obj.Current_url('https://192.168.254.204/kdemo/index.php')
