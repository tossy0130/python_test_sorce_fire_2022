import sys
import tkinter

from distutils import bcppcompiler
from tkinter import messagebox
import requests
from bs4 import BeautifulSoup

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

import subprocess
from subprocess import PIPE

import win32com.client

import datetime

# ================ サイボウズ　開く

to_date = datetime.datetime.now()
change_date = to_date.strftime("%Y-%m-%d")

print(change_date)

date_arr = [
    {'year': 2019, 'name': '令和', 'new_Japanese_calendar': '平成31年'},
    {'year': 1986, 'name': '平成', 'new_Japanese_calendar': '平成元年'},
    {'year': 1926, 'name': '昭和', 'new_Japanese_calendar': '大正15年'}
]

now_y = change_date[:4]
print(now_y)


def Gengou(now_y):
    for d_val in date_arr:
        if now_y == d_val['year']:
            print('333')
            print(d_val['new_Japanese_calendar'])
            # 年度の元年を返す
            return d_val['new_Japanese_calendar']

        if int(now_y) >= d_val['year']:
            year = int(now_y) - d_val['year'] + 1
            return d_val['name'] + str(year) + "年"


def btn_01_Click():

    try:

        # selenium での　chrome の実行ファイル　指定
        driver = webdriver.Chrome(
            executable_path=r'C:\\chromedriver_win32\\chromedriver.exe')

        # ～いろいろな処理～
        driver.get("https://hhj4p.cybozu.com/login")

        user_id_s = driver.find_element(By.NAME, "username")  # name 属性取得
        pass_word_s = driver.find_element(By.NAME, "password")  # name 属性取得

        user_id_s.clear()
        pass_word_s.clear()

        user_id_s.send_keys("ログインID")  # name 属性に値をセット
        pass_word_s.send_keys("パス")  # name 属性に値をセット

        user_id_s.submit()  # form を submit する。

        time.sleep(1.2)

        # test = driver.find_element(
        #    By.CSS_SELECTOR, "body > div.container-slash > div > div.contents - \
        #    left-slash.services-slash > div > a")

        test = driver.find_element(By.CLASS_NAME, 'service-slash')
        test.click()

        time.sleep(1.2)

        driver.find_element(
            By.XPATH, "//*[@id ='appIconMenuFrame']/div[2]/nav/ul/li[2]/span/a").click()

        time.sleep(0.8)

        driver.get(driver.current_url)
    finally:
        os.kill(driver.service.process.pid, signal.SIGTERM)


# ================= outlook 開く
def btn_02_Click():
    subprocess.Popen(
        r"C:\\Program Files\\Microsoft Office\\root\\Office16\\OUTLOOK.EXE")


# ================ outlook 操作
def out_look_01():

    # メール　テンプレートファイル　パス
    text_file_path = r"D:\\斎場\\津市\\2022_保守メールテンプレ.txt"

    # メールテンプレート　変更 text
    date_tmp = datetime.datetime.now()
    month_text = date_tmp.strftime("%Y年%m月%d日")

    print(month_text)

    tmp_date = Gengou(now_y)  # 　西暦 => 令和　変換
    print(tmp_date)

    # ファイル読み込み
    read_file = open(text_file_path, "r", encoding='utf-8_sig')
    read_file = read_file.read()

   # mail_body = read_file.replace("実施日：令和4年09月21日 16:45～17:45", )

    # Outlookのmailオブジェクト設定
    outlook = win32com.client.Dispatch('Outlook.Application')
    objMail = outlook.CreateItem(0)  # MailItemオブジェクトのID

    # 送り先メールアドレス


root = tkinter.Tk()

root.title(u"PC バケット")
root.geometry("600x300")

# ================ サイボウズ　起動
# 画像ファイルをインスタンス変数に代入
img = tkinter.PhotoImage(file="python/Tkinter/img/s_img.png")
small_img = img.subsample(2, 2)

# ボタン　設定
btn_01 = tkinter.Button(root, text="画像", image=small_img,
                        width="180", command=btn_01_Click)
btn_01.place(x=20, y=20)
# ================ サイボウズ　起動 END

# ================ outlook　起動
img_02 = tkinter.PhotoImage(file="python/Tkinter/img/outlook.png")
small_img_02 = img_02.subsample(2, 2)

btn_02 = tkinter.Button(root, text="outlook", image=small_img_02,
                        width=180, command=btn_02_Click)

btn_02.place(x=240, y=20)
# ================ outlook　起動 END

# ================ テンプレメール ボタン
btn_03 = tkinter.Button(root, text="メール", width=100, command=out_look_01)
btn_03.place(x=20, y=200)

root.mainloop()
