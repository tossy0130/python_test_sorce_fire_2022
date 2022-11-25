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


#　元ファイル用 ディレクトリ
DIR_PATH = 'python/test_02/back_up/'
# 比較ファイル用 ディレクトリ
DIR_PATH_HIKAKU = 'python/test_02/back_up02/'

LOG_DIR = 'python/test_02/log/'


def check_dir(get_path):
    # ファイル・フォルダチェック

    try:
        # フォルダが存在していた場合
        if(os.path.isdir(get_path)):
            pass
        else:
            os.makedirs(get_path)
    except FileExistsError:
        print('ファイル作成：：：例外処理')


class Date_To():
    # ============ 日時・時刻　クラス　============
    # 予約時間　格納用
    def __init__(self):
        self.time_num = [
            ['1', '9:00'],
            ['2', '10:00'],
            ['3', '11:00'],
            ['4', '12:00'],
            ['5', '13:00'],
            ['6', '14:00'],
            ['7', '15:00']
        ]

        self.dt_now = ""

    # === 当日取得 ::: 2022-11-04 14:26:56.878021
    def Now_date(self):
        self.dt_now = datetime.datetime.now()
        return self.dt_now

    # === 日付 ::: フォーマット 22-11-04
    def Date_cut(self, t_date):
        now_date = t_date
        n_now_date = now_date.strftime("%y-%m-%d")
        return n_now_date

    # === index に応じた time_num の時間を出力
    def Yoyaku_Time_idx(self, idx, idx_02):
        return self.time_num[idx][idx_02]

    # === 当日から num　を加算した値を返す
    def Date_Add(self, num):
      #  self.dt_now = datetime.datetime.now()
        date_add = self.dt_now + datetime.timedelta(days=num)
        return date_add
        # Date_To ****** END ********


def Set_Name_Val(name, set_val):
    # === name に値を入れる
    tmp_name = driver.find_element(By.NAME, name)  # name 属性取得
    tmp_name.clear()
    tmp_name.send_keys(set_val)  # name 属性に値をセット


def Sub_Mit(name):
    tmp_name = driver.find_element(By.NAME, name)  # name 属性取得
    tmp_name.submit()


# ========================

# === reserve_edit.php での「データクレンジング」
# 火葬予約日時 name（yoyakubi_date）, 火葬受付番号 name（renban） を空にする
def Create_File_view_list(url, file_name):

    # # === 時刻取得

    # driver.find_elements(By.CLASS_NAME, "underline")

    # 日付け
    yoyaku_date_01 = []

    # 全部消えた
#    for i in range(4, 7, 1):
#        yoyaku_date_01 = driver.find_elements(
#            By.CSS_SELECTOR, f"#form1 > table > tbody > tr:nth-child({i}) > td:nth-child(2)")

    html_text = driver.page_source  # selenium

# === 予約 × 削除
    yoyaku_01 = driver.find_element(
        By.CSS_SELECTOR, "#form1 > table > tbody > tr:nth-child(4) > td:nth-child(2)")
    yoyaku_02 = driver.find_element(
        By.CSS_SELECTOR, "#form1 > table > tbody > tr:nth-child(5) > td:nth-child(2)")
    yoyaku_03 = driver.find_element(
        By.CSS_SELECTOR, "#form1 > table > tbody > tr:nth-child(6) > td:nth-child(2)")

    # ================== URL から、 原本 HTMLファイル、 比較用 HTMLファイル作成
    get_url = url

    # === ファイルが存在していなかったら、原本ファイル作成
    # ファイル存在チェック
    if os.path.exists(DIR_PATH + file_name):  # python/test/back_up
        # === ファイルが存在していたら、比較用　ファイル作成
        File_Write(DIR_PATH_HIKAKU + file_name, html_text)  # ファイル書き込み関数

        # ====== value を空にする =======
        with open(DIR_PATH_HIKAKU + file_name, encoding='utf-8') as f:
            data_lines = f.read()

            # 2022年11月9日(水) 19:35現在の空き状況 => 空にする
            # data_lines = data_lines.replace(yoyakubi_date.text, '')
            # data_lines = data_lines.replace(renban.text, '')

            # === 日付けデータ　置換

         #   data_lines = data_lines.replace(yoyaku_date_01.text, '')

            # name = yoyakubi_data の value を空にする
            # data_lines = data_lines.replace(
            #    "value=\"" + str(yoyakubi_date_val) + "\"" + ">", "value=\"\"")

            # data_lines = data_lines.replace('Changed', '変更')
            # data_lines = data_lines.replace('Deleted', '削除')

        with open(DIR_PATH_HIKAKU + file_name, mode='w', encoding='utf-8') as f:
            f.write(data_lines)

    else:
        # === ファイルが存在していなかったら、原本ファイル作成
        File_Write(DIR_PATH + file_name, html_text)  # ファイル書き込み関数

        # ====== value を空にする =======
        with open(DIR_PATH + file_name, encoding='utf-8') as f:
            data_lines = f.read()

            # 2022年11月9日(水) 19:35現在の空き状況 => 空にする
            # data_lines = data_lines.replace(yoyakubi_date.text, '')
            # data_lines = data_lines.replace(renban.text, '')

            # === 日付けデータ　置換
        #    for yoyaku_val in yoyaku_date_01:
        #        data_lines = data_lines.replace(yoyaku_val.text, '')

            # === 予約テスト　×　削除
            data_lines = data_lines.replace(yoyaku_01.text, '')
            data_lines = data_lines.replace(yoyaku_02.text, '')
            data_lines = data_lines.replace(yoyaku_03.text, '')

            # name = yoyakubi_data の value を空にする
            # data_lines = data_lines.replace(
            #    "value=\"" + str(yoyakubi_date_val) + "\"" + ">", "value=\"\"")

            # data_lines = data_lines.replace('Changed', '変更')
            # data_lines = data_lines.replace('Deleted', '削除')

        with open(DIR_PATH + file_name, mode='w', encoding='utf-8') as f:
            f.write(data_lines)

# ================

# ====== ファイル書き込み


def File_Write(path_w, get_text):
    # ================== ファイル書き込み
    with open(path_w, mode='wb') as f:
        for item in get_text:
            f.write(item.encode('utf-8'))

# ====== ファイル追記


def File_Append(path_w, get_text):
    # ================= ファイル追記
    with open(path_w, mode='ab') as f:
        for item in get_text:
            f.write(item.encode('utf-8'))


# ======================= 作業 Start ======================
# === ディレクトリ作成
check_dir(DIR_PATH)  # 原本 ディレクトリ
check_dir(DIR_PATH_HIKAKU)  # 比較用 ディレクトリ
check_dir(LOG_DIR)  # エラー時、log.txt 格納用　ディレクトリ

# webManager 使用
driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://192.168.254.204/kdemo/index.php")


btn_01 = driver.find_element(
    By.XPATH, "//*[@id='form1']/div[1]/ul/li[2]/a").click()
time.sleep(0.6)

# ======= view_list.php

py_btn_02 = driver.find_element(By.ID, "py_btn_02").click()
time.sleep(0.6)

# === ＊＊＊＊＊＊＊＊＊＊＊＊ login.php

user_id = driver.find_element(By.NAME, "user_id")  # name 属性取得
pass_word = driver.find_element(By.NAME, "password")  # name 属性取得

user_id.clear()
pass_word.clear()

user_id.send_keys("jimcom35")  # name 属性に値をセット
pass_word.send_keys("Jim357221")  # name 属性に値をセット

user_id.submit()  # form を submit する。

# ================== view_list.php　、　「火葬タイプ」 「予約日」　指定　==================

time.sleep(2.6)

Create_File_view_list(driver.current_url, 'view_list.txt')
