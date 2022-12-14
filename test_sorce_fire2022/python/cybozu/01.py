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

import signal

import os


class Saibouzu:

    def __init__(self, s_username, s_password):
        self.s_username = s_username
        self.s_password = s_password

    def Saibouzu_Login(self):
        # selenium での　chrome の実行ファイル　指定
        driver = webdriver.Chrome(
            executable_path=r'C:\\chromedriver_win32\\chromedriver.exe')

        try:
            driver.get("https://hhj4p.cybozu.com/login")

            user_id_s = driver.find_element(
                By.NAME, 'username')  # name 属性取得
            pass_word_s = driver.find_element(
                By.NAME, 'password')  # name 属性取得

            user_id_s.clear()
            pass_word_s.clear()

            user_id_s.send_keys(self.s_username)  # name 属性に値をセット
            pass_word_s.send_keys(self.s_password)  # name 属性に値をセット

            user_id_s.submit()  # form を submit する。

            time.sleep(1.2)

            test = driver.find_element(By.CLASS_NAME, 'service-slash')
            test.click()

            time.sleep(1.2)

            driver.find_element(
                By.XPATH, "//*[@id ='appIconMenuFrame']/div[2]/nav/ul/li[2]/span/a").click()

            time.sleep(0.8)

            driver.get(driver.current_url)

        finally:
            os.kill(driver.service.process.pid, signal.SIGTERM)

# ========== サイボウズへログイン開始


Saibouz_Obj = Saibouzu('自分のサイボウズ ログインID', '自分のサイボウズの パスワード')
Saibouz_Obj.Saibouzu_Login()
