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

from selenium.webdriver.chrome import service as fs
from selenium.webdriver.common.by import By
import chromedriver_binary
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

# ========= ログファイル用　格納ディレクトリ
#　元ファイル用 ディレクトリ
DIR_PATH = './python_TSU/test/back_up/'
# 比較ファイル用 ディレクトリ
DIR_PATH_HIKAKU = './python_TSU/test/back_up02/'


def Check_DIR(path):
    # ====== ログ用 格納フォルダ を作成・作成済みの場合は、何も処理しない
    tmp_path = path

    try:
        if(os.path.isdir(tmp_path)):  # フォルダが存在していた場合
            pass
        else:
            os.makedirs(tmp_path)
    except FileExistsError:
        print('実行関数:Check_DIR ::: ディレクトリ作成エラー')


def File_Write(path_w, get_text):
    # ================== ファイル書き込み
    with open(path_w, mode='wb') as f:
        for item in get_text:
            f.write(item.encode('utf-8'))


def GET_Scraping_Requests(url, file_name):
    # ================== URL から、 原本 HTMLファイル、 比較用 HTMLファイル作成
    get_url = url

   # =========== BeautifulSoup
   # response = requests.get(get_url, verify=False)
   # html_text = BeautifulSoup(response.text, 'html.parser')

    html_text = driver.page_source  # selenium
    # html_text = BeautifulSoup(response.text, 'lxml')

    # ファイル存在チェック
    if os.path.exists(DIR_PATH + file_name):  # python/test/back_up
        # === ファイルが存在していたら、比較用　ファイル作成
        File_Write(DIR_PATH_HIKAKU + file_name, html_text)  # ファイル書き込み関数
    else:
        # === ファイルが存在していなかったら、原本ファイル作成
        File_Write(DIR_PATH + file_name, html_text)  # ファイル書き込み関数


def Set_Name_Val(name, set_val):
    # === name に値を入れる
    tmp_name = driver.find_element(By.NAME, name)  # name 属性取得
    tmp_name.clear()
    tmp_name.send_keys(set_val)  # name 属性に値をセット


def Set_Name_Val_Select(name, idx):
    # === name に値を入れる  select の値を index で指定
    tmp_name = driver.find_element(By.NAME, name)  # name 属性取得
    Select_Itme = Select(tmp_name)
    Select_Itme.select_by_index(idx)  # name 属性に値をセット


class Date_To():
    # ============ 日時・時刻　クラス　============
    # 予約時間　格納用
    def __init__(self):
        self.time_num = [
            ['3', '9:00'],
            ['4', '9:30'],
            ['5', '10:00'],
            ['6', '11:00'],
            ['7', '11:30'],
            ['8', '12:00'],
            ['9', '12:30'],
            ['10', '13:30'],
            ['11', '14:00'],
            ['12', '14:30'],
            ['13', '15:00']
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
        self.dt_now = datetime.datetime.now()
        date_add = self.dt_now + datetime.timedelta(days=num)
        return date_add

# ===============================================================
# ====================================== 実行 ===================
# ===============================================================


# ログ用ディレクトリ作成
Check_DIR(DIR_PATH)
Check_DIR(DIR_PATH_HIKAKU)

driver = webdriver.Chrome(ChromeDriverManager().install())

# === ターゲット URL
driver.get("https://www.itsukushiminomori.jp/yoyaku/index.php")

html = driver.page_source
print('html:::' + html)

driver.find_element(By.XPATH,
                    "//*[@id='form1']/div[1]/ul/li[2]/a").click()

# ===================================
# ===================== view_list.php
# ===================================
time.sleep(1.0)

# === スクレイピング処理 実行 & ログファイル　出力
GET_Scraping_Requests(driver.current_url, 'view_list.php')

driver.find_element(By.XPATH,
                    "/html/body/div[2]/form/div[1]/a[1]").click()

# ===================================
# ===================== login.php
# ===================================
time.sleep(1.0)

# === スクレイピング処理 実行 & ログファイル　出力
GET_Scraping_Requests(driver.current_url, 'login.php')

user_id = driver.find_element(By.NAME, "user_id")  # name 属性取得
pass_word = driver.find_element(By.NAME, "password")  # name 属性取得

user_id.clear()
pass_word.clear()

user_id.send_keys("JIM_natsume")  # name 属性に値をセット
pass_word.send_keys("jimjim")  # name 属性に値をセット

user_id.submit()  # form を submit する。

# ===================================
# ===================== view_list.php 、 ログイン済み
# ===================================
time.sleep(1.0)

# === スクレイピング処理 実行 & ログファイル　出力
GET_Scraping_Requests(driver.current_url, 'view_list(login).php')

# ラジオボタン ==　式場利用	利用しない
driver.find_element(By.XPATH,
                    "/html/body/div[2]/form/table/tbody/tr[1]/td[2]/label[1]/input").click()

# ========== 日付け・時間  実行 ==========
Date_Obj = Date_To()  # クラスオブジェクト

date_add = Date_Obj.Date_Add(7)  # 当日から、 7日　プラスした　日付けを取得
format_date_add = Date_Obj.Date_cut(date_add)  # 23-01-01 形式へ変換
print('format_date_add:::' + format_date_add)

form_send_date = Date_Obj.Yoyaku_Time_idx(10, 0)  # 13
form_send_time = Date_Obj.Yoyaku_Time_idx(10, 1)  # 15:00

# submit用 JavaScript へ 値を渡す
driver.execute_script(
    "javascript:main.set3KeyAndSubmit('form1', 'reserve_entry', 'YOYAKUBI'," + "\'" + format_date_add + "\'" + ", 'WAKU_NO', " + "\'" + form_send_date + "\'" + ", 'YOYAKU_TIME', " + "\'" + form_send_time + "\'" + ');return false;')


# ===================================
# ===================== reserve_edit.php
# ===================================

time.sleep(1.0)

# === スクレイピング処理 実行 & ログファイル　出力
GET_Scraping_Requests(driver.current_url, 'reserve_edit.php')

# ======================== フォームに値セット

# === 待合室利用
driver.find_element(By.XPATH,
                    "/html/body/div[2]/form/table[1]/tbody/tr[2]/td/span[2]/label[4]/input").click()

# === 申請者情報
Set_Name_Val('applicant_name01', '織田')  # 申請者氏名 性
Set_Name_Val('applicant_name02', '信長')  # 　申請者氏名 名

Set_Name_Val('applicant_kana01', 'オダ')  # 申請者カナ 性
Set_Name_Val('applicant_kana02', 'ノブナガ')  # 申請者カナ 名

Set_Name_Val('applicant_tel01', '0256')  # 連絡先TEL 01
Set_Name_Val('applicant_tel02', '11')  # 連絡先TEL 02
Set_Name_Val('applicant_tel03', '9999')  # 連絡先TEL 03

Set_Name_Val('applicant_zip01', '955')  # 郵便番号 01
Set_Name_Val('applicant_zip02', '0092')  # 郵便番号 02

Set_Name_Val('applicant_address1', '新潟県三条市須頃３丁目７４')  # 住所 01
Set_Name_Val('applicant_address2', '')  # 住所 02 番地以降

# === ブラウザ　移動
driver.execute_script("window.scrollTo(0, 1000);")
time.sleep(0.5)


# === 死亡者情報
Set_Name_Val('dead_name01', '織田')  # 死亡者氏名　性
Set_Name_Val('dead_name02', '信秀')  # 死亡者氏名 名

Set_Name_Val('dead_kana01', 'オダ')  # 死亡者カナ　性
Set_Name_Val('dead_kana01', 'ノブヒデ')  # 死亡者カナ 名

# 性別
driver.find_element(By.XPATH,
                    "/html/body/div[2]/form/table[3]/tbody/tr[3]/td/span[2]/label[1]/input").click()


Set_Name_Val_Select('dead_birth_koyomi_type', 1)
Set_Name_Val('dead_birth_year', '1930')
Set_Name_Val_Select('dead_birth_month', 1)
Set_Name_Val_Select('dead_birth_day', 3)

Set_Name_Val_Select('dead_koyomi_type', 2)
Set_Name_Val('dead_year', '5')
Set_Name_Val_Select('dead_month', 3)
Set_Name_Val_Select('dead_day', 1)


Set_Name_Val('dead_zip01', '955')  # 郵便番号 01
Set_Name_Val('dead_zip02', '0092')  # 郵便番号 02

Set_Name_Val('dead_address1', '新潟県三条市須頃３丁目７４')
Set_Name_Val('dead_address2', '')

driver.execute_script(
    "main.setModeAndSubmit('form1', 'entry_confirm')")
