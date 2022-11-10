import datetime
import datetime as dt
from importlib.resources import path

import requests
from bs4 import BeautifulSoup, BeautifulStoneSoup

from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from smtplib import SMTP
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formatdate
from email.mime.text import MIMEText  # MIME 形式データ用
from email.utils import formatdate
import smtplib

import os


def Print_NamiNami():
    print("=========================================================" + '\n' +
          "=========================================================" + '\n' +
          "=========================================================")


# selenium での　chrome の実行ファイル　指定
driver = webdriver.Chrome(
    executable_path=r'C:\\chromedriver_win32\\chromedriver.exe')

driver.get("https://192.168.254.204/kdemo/index.php")


html_text = driver.page_source
print('html_text:::' + html_text)


# ================================= index.php

# === xpath 取得方法
# xpath = '//*[@id="header_line"]/a'
# element_01 = driver.find_element(By.XPATH, xpath)


# === CSS セレクター 取得方法

kw_search = driver.find_element(
    By.CSS_SELECTOR, "#header_line > a")
print('kw_search:::' + kw_search.text)

btn_area = driver.find_element(By.CSS_SELECTOR, "#form1 > div.btn_area")
print('.btn_area:::' + btn_area.text)

i_div_strong = driver.find_element(
    By.CSS_SELECTOR, "#form1 > div:nth-child(4)")
print('div.strong:::' + i_div_strong.text)


#main > span
