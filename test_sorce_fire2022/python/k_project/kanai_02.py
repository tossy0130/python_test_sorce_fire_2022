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


def Clicl_Check_CSS_SELECTOR(Css_Selector):
    # ========= click チェック
    if int(len(driver.find_elements(
            By.CSS_SELECTOR, Css_Selector)) > 0):

        driver.find_elements(
            By.CSS_SELECTOR, Css_Selector)[0].click()
    else:
        print('要素なし')


# selenium での　chrome の実行ファイル　指定
driver = webdriver.Chrome(
    executable_path=r'C:\\chromedriver_win32\\chromedriver.exe')

driver.get("https://toriatsukai.kanai-marukin.com/")

# === 実行
Check_handles('//*[@id="cont"]/center/div[1]/iframe')
# click
driver.find_element(By.CSS_SELECTOR, "body > div > div.m_item2 > a").click()
time.sleep(0.5)

# ================== 「取扱品」 ====================

# === 実行
Check_handles('//*[@id="cont"]/center/div[2]/iframe')
# click
driver.find_element(
    By.CSS_SELECTOR, "body > table:nth-child(9) > tbody > tr:nth-child(4) > td:nth-child(1) > a").click()

time.sleep(0.8)

# カテゴリ １１８・ハッカーケース
Check_handles('//*[@id="cont"]/center/div[2]/iframe')
# click
driver.find_element(
    By.CSS_SELECTOR, "body > table:nth-child(6) > tbody > tr:nth-child(2) > td:nth-child(1) > a").click()

time.sleep(0.8)

# === 画像パス　取得
img = driver.find_element(By.TAG_NAME, "img")
img_src = img.get_attribute('src')
print('画像パス:::' + img_src)

time.sleep(0.8)

# === 戻る

# ====== タブを移動して、新規タブを閉じる =======
driver.switch_to.window(driver.window_handles[1])
driver.close()

time.sleep(0.8)

Check_handles('//*[@id="cont"]/center/div[2]/iframe')

# click チェック
Clicl_Check_CSS_SELECTOR(
    'body > table:nth-child(6) > tbody > tr:nth-child(32) > td:nth-child(1) > a')

# driver.find_element(
#    By.CSS_SELECTOR, "body > table:nth-child(6) > tbody > tr:nth-child(32) > td:nth-child(1) > a").click()

time.sleep(0.8)

# === 画像パス　取得
img = driver.find_element(By.TAG_NAME, "img")
img_src = img.get_attribute('src')
print('画像パス:::' + img_src)

time.sleep(0.8)

# ====== タブを移動して、新規タブを閉じる =======
driver.switch_to.window(driver.window_handles[1])
driver.close()

time.sleep(0.8)

Check_handles('//*[@id="cont"]/center/div[2]/iframe')

# click チェック
Clicl_Check_CSS_SELECTOR(
    'body > table:nth-child(6) > tbody > tr:nth-child(32) > td:nth-child(2) > a')

time.sleep(0.8)
