import datetime
import datetime as dt
from genericpath import isfile
from importlib.resources import path
from opcode import opname

import requests
from bs4 import BeautifulSoup, BeautifulStoneSoup

from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager
# pip install webdriver_manager

from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC

from smtplib import SMTP
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formatdate
from email.mime.text import MIMEText  # MIME 形式データ用
from email.utils import formatdate
import smtplib

import difflib


import os

# ================= iframe 突破用 ================


def Check_handles(x_path):
    handles = driver.window_handles
    flg = False
    for i in range(len(handles)):
        if flg:
            break
        try:
            driver.switch_to.window(handles[i])
            iframe = driver.find_element(
                By.XPATH, x_path)
            driver.switch_to.frame(iframe)
            flg = True
        except:
            pass


def Selenium_HTML_Print():
    html = driver.page_source
    print('html:::' + html)


# selenium での　chrome の実行ファイル　指定
driver = webdriver.Chrome(
    executable_path=r'C:\\chromedriver_win32\\chromedriver.exe')

driver.get("https://toriatsukai.kanai-marukin.com/")

# === 実行
Check_handles('//*[@id="cont"]/center/div[1]/iframe')

# click
driver.find_element(By.CSS_SELECTOR, "body > div > div.m_item2 > a").click()

time.sleep(1.0)

# ================== 「取扱品」 ====================

# === 実行
Check_handles('//*[@id="cont"]/center/div[2]/iframe')

# click
driver.find_element(
    By.CSS_SELECTOR, "body > table:nth-child(7) > tbody > tr:nth-child(2) > td:nth-child(1) > a").click()

time.sleep(1.0)

# ================= 「取扱商品 カテゴリー」 =============
Check_handles('//*[@id="cont"]/center/div[2]/iframe')

time.sleep(0.5)

Selenium_HTML_Print()

# ========= タグ　取得　テスト
a_tag = driver.find_elements(By.TAG_NAME, "a")
for val in a_tag:
    print(val.text)

img = driver.find_elements(By.TAG_NAME, "img")
for img_val in img:
    tmp = img_val.get_attribute('src')
    print(tmp)

font_tag = driver.find_elements(By.TAG_NAME, "font")
for font_val in font_tag:
    print(font_val.text)

# iframe = driver.find_element(By.TAG_NAME, "iframe")

# iframe = driver.find_element(
#    By.CSS_SELECTOR, "#cont > center > div.top > iframe")

# driver.switch_to.frame(iframe)

# html = driver.page_source
# print('html:::' + html)

# driver.find_element(By.CSS_SELECTOR, "body > div > div.m_item2 > a").click()

# print('test:::' + test)

# iframe = driver.find_element(
#    By.XPATH, "/html/body/div/div[3]/a")

# driver.find_element(
#    By.XPATH, "/html/body/div/div[3]/a").click()

# driver.find_element(By.CSS_SELECTOR, "body > div > div.m_item2 > a").click()

# driver.find_element(By.CLASS_NAME, 'm_item2').click()
