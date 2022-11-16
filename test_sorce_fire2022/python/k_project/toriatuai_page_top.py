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

from webdriver_manager.chrome import ChromeDriverManager


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


# webManager 使用
driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://toriatsukai.kanai-marukin.com/")

# === 実行
Check_handles('//*[@id="cont"]/center/div[1]/iframe')

# click
driver.find_element(By.CSS_SELECTOR, "body > div > div.m_item2 > a").click()
time.sleep(2.0)

# =============== 取扱商品　トップページ取得 ================
# === 実行
Check_handles('//*[@id="cont"]/center/div[2]/iframe')

font_tag = driver.find_elements(By.TAG_NAME, "font")
a_tag = driver.find_elements(By.TAG_NAME, "a")

img = driver.find_elements(By.TAG_NAME, 'img')


for img_val in img:
    img_src = img_val.get_attribute('src')
    print(img_src)

for font_val in font_tag:
    print(font_val.text)
