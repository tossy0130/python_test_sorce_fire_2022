import requests
from bs4 import BeautifulSoup, BeautifulStoneSoup

from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from urllib.request import urlopen
from urllib.error import HTTPError

import os

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
    global driver
    driver = webdriver.Chrome(
        executable_path=r'C:\\chromedriver_win32\\chromedriver.exe')

    # カレントの URL 取得
    def Current_url(self, url):
        print(url)
        print('カレントURL:::' + driver.current_url)
        print('カレントURL:::02:::' + url)


class File_Operation():

    # ファイルのパスを指定
    def __init__(self, file_path):
        self.f_path = file_path

    # ディレクトリチェックをして、ディレクトリがなかったら作成
    def File_create(self):

        try:
            if (os.path.isdir(self.f_path)):
                pass
            else:
                # *** makedirs => 途中のフォルダも作成 ***
                os.makedirs('python/class/back_up/')
        except FileExistsError:
            print('File_create エラー')

# url_open

# === urlopen で　取得


def Url_open_get(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        print(e)
    else:
        print('HTML 取得成功')
        print(html)


Url_open_get('https://192.168.254.204/kdemo/index.php')

# ファイル作成
# バックアップファイルの、パスを設定
File_obj = File_Operation('python/class/back_up/')  # ディレクトリパス
File_obj.File_create()  # ディレクトリ作成


Sel_obj = Selenium_Test()
Sel_obj.Current_url('https://192.168.254.204/kdemo/index.php')
