import datetime
import datetime as dt
from genericpath import isfile
from importlib.resources import path
from opcode import opname

import requests
from bs4 import BeautifulSoup, BeautifulStoneSoup

from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


from smtplib import SMTP
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formatdate
from email.mime.text import MIMEText  # MIME 形式データ用
from email.utils import formatdate
import smtplib

import difflib

import sys
import os
import re

# webManager 使用
driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://192.168.254.204/kdemo/index.php")

# ========= index.php =========

html_text = driver.page_source
# === 正規表現でテキスト削除
result_01 = re.sub(r'(?<=<div class="alignL">).*?(?=<\/div>)', "", html_text)
result_02 = re.sub(r'(?<=<span id="notice_01">).*?(?=<\/span>)', "", result_01)

# ========= view_list.php =========

btn_01 = driver.find_element(
    By.XPATH, "//*[@id='form1']/div[1]/ul/li[2]/a").click()

time.sleep(0.6)

py_btn_02 = driver.find_element(By.ID, "py_btn_02").click()
time.sleep(0.6)

# === ＊＊＊＊＊＊＊＊＊＊＊＊ login.php

user_id = driver.find_element(By.NAME, "user_id")  # name 属性取得
pass_word = driver.find_element(By.NAME, "password")  # name 属性取得

user_id.clear()
pass_word.clear()

user_id.send_keys("")  # name 属性に値をセット
pass_word.send_keys("")  # name 属性に値をセット

user_id.submit()  # form を submit する。

# ========= view_list.php =========

time.sleep(0.6)

html_view_list_source = driver.page_source

# === 正規表現でテキスト削除
html_view_list_source_01 = re.sub(
    r'(?<=<span class="strong">).*?(?=</span>)', "", html_view_list_source)

html_view_list_source_02 = re.sub(
    r'(?<=<td class="alignC">).*?(?=</td>)', "", html_view_list_source_01)

html_view_list_source_03 = re.sub(
    r'(?<=<th class="alignC" style="word-wrap:break-word; text-indent:3px;">).*?(?=</th>)', "", html_view_list_source_02)
print(html_view_list_source_03)


py_btn_02 = driver.find_element(By.ID, "py_btn_02").click()
time.sleep(4.6)
# ====================================================
# ================ reserve_list.php ==================
# ====================================================

html_reserve_list_sorce = driver.page_source
print(html_reserve_list_sorce)
