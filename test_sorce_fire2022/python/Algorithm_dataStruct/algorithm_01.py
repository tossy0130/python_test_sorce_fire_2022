import os
import pandas as pd

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

import numpy as np


# ========================== 二分探索

def binary_search(data, value):
    left = 0
    right = len(data) - 1  # 探索する範囲の右端を設定
    while left <= right:
        mid = (left + right) // 2
        if data[mid] == value:  # === 探索完了
            return mid
        elif data[mid] < value:
            left = mid + 1
        else:
            right = mid - 1
    return -1               # 見つからない場合


print("=== 二分探索 ===")
data = [10, 20, 30, 40, 50, 60, 70, 80, 90]

print(binary_search(data, 70))

# ========================== バブルソート

for i in range(len(data)):
    for j in range(len(data) - i - 1):
        if data[j - 1] > data[i]:
            data[i], data[i - 1] = data[i - 1], data[i]

print("=== バブルソート ===")
print(data)
