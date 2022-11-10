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


# 日付け・時刻　除外　テスト ディレクトリ
DIR_PATH = 'python/view_list_test/'

DIR_PATH_2 = 'python/reserve_list_test/'


def Print_NamiNami():
    print("=========================================================" + '\n' +
          "=========================================================" + '\n' +
          "=========================================================")


def Check_Dir(path):
    # ==================　path　の場所に ディレクトリ作成
    d_path = path

    try:
        if(os.path.isdir(d_path)):  # フォルダが存在していた場合
            pass
        else:
            os.makedirs(d_path)
    except FileExistsError:
        print('関数名:Check_Dir ::: ディレクトリ作成エラー')


# === reserve_list.php , view_list.php での「データクレンジング」
def Create_File_01(url, file_name):

    # # === 時刻取得
    main_span = driver.find_element(
        By.CSS_SELECTOR, "#main > span")
    print('main_span :::' + main_span.text)

    # ================== URL から、 原本 HTMLファイル、 比較用 HTMLファイル作成
    get_url = url

    html_text = driver.page_source  # selenium

    # === ファイルが存在していなかったら、原本ファイル作成
    File_Write(DIR_PATH + file_name, html_text)  # ファイル書き込み関数

    with open(DIR_PATH + file_name, encoding='utf-8') as f:
        data_lines = f.read()

        # 2022年11月9日(水) 19:35現在の空き状況 => 空にする
        data_lines = data_lines.replace(main_span.text, '')

        # 予約日数字 5 ～ 1 , ×　=> 空にする
        data_lines = data_lines.replace(
            "return false;\">1</a>", "return false;\"></a>")
        data_lines = data_lines.replace(
            "return false;\">2</a>", "return false;\"></a>")
        data_lines = data_lines.replace(
            "return false;\">3</a>", "return false;\"></a>")
        data_lines = data_lines.replace(
            "return false;\">4</a>", "return false;\"></a>")
        data_lines = data_lines.replace(
            "return false;\">5</a>", "return false;\"></a>")
        data_lines = data_lines.replace(
            "return false;\">×</a>", "return false;\"></a>")

       # data_lines = data_lines.replace('Changed', '変更')
       # data_lines = data_lines.replace('Deleted', '削除')

    with open(DIR_PATH + file_name, mode='w', encoding='utf-8') as f:
        f.write(data_lines)


# === reserve_edit.php での「データクレンジング」
# 火葬予約日時 name（yoyakubi_date）, 火葬受付番号 name（renban） を空にする
def Create_File_02(url, file_name):

    # # === 時刻取得
    yoyakubi_date = driver.find_element(By.NAME, "yoyakubi_date")
    renban = driver.find_element(By.NAME, "renban")

    # ================== URL から、 原本 HTMLファイル、 比較用 HTMLファイル作成
    get_url = url

    html_text = driver.page_source  # selenium

    # === ファイルが存在していなかったら、原本ファイル作成
    File_Write(DIR_PATH + file_name, html_text)  # ファイル書き込み関数

    with open(DIR_PATH + file_name, encoding='utf-8') as f:
        data_lines = f.read()

        # 2022年11月9日(水) 19:35現在の空き状況 => 空にする
        data_lines = data_lines.replace(yoyakubi_date.text, '')
        data_lines = data_lines.replace(renban.text, '')

        # 予約日数字 5 ～ 1 , ×　=> 空にする
        # data_lines = data_lines.replace(
        #    "return false;\">1</a>", "return false;\"></a>")

        # data_lines = data_lines.replace('Changed', '変更')
        # data_lines = data_lines.replace('Deleted', '削除')

    with open(DIR_PATH + file_name, mode='w', encoding='utf-8') as f:
        f.write(data_lines)


def File_Write(path_w, get_text):
    # ================== ファイル書き込み
    with open(path_w, mode='wb') as f:
        for item in get_text:
            f.write(item.encode('utf-8'))


# ディレクトリ　作成
Check_Dir(DIR_PATH)


# selenium での　chrome の実行ファイル　指定
driver = webdriver.Chrome(
    executable_path=r'C:\\chromedriver_win32\\chromedriver.exe')

driver.get("https://192.168.254.204/kdemo/index.php")

html_text = driver.page_source
print('html_text:::' + html_text)

# click イベント
btn_01 = driver.find_element(By.ID, "test_01_btn").click()
time.sleep(0.6)

# === view_list.php

print("カレントURL_2 view_list:::" + driver.current_url)

py_btn_02 = driver.find_element(By.ID, "py_btn_02").click()
time.sleep(0.6)

html_text2 = driver.page_source
print('html_text2:::' + html_text2)

Print_NamiNami()

user_id = driver.find_element(By.NAME, "user_id")  # name 属性取得
pass_word = driver.find_element(By.NAME, "password")  # name 属性取得

user_id.clear()
pass_word.clear()

user_id.send_keys("jimcom35")  # name 属性に値をセット
pass_word.send_keys("Jim357221")  # name 属性に値をセット

user_id.submit()  # form を submit する。

time.sleep(2.6)

# === クラス名で取得

main_span = driver.find_element(
    By.CSS_SELECTOR, "#main > span")
print('main_span :::' + main_span.text)


Create_File_01(driver.current_url, 'view_list.txt')
