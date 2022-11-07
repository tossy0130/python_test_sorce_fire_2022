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

#　元ファイル用 ディレクトリ
DIR_PATH = 'python/test/back_up/'
# 比較ファイル用 ディレクトリ
DIR_PATH_HIKAKU = 'python/test/back_up02/'

URL_ARR = []


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


def GET_Scraping_Requests(url, file_name):
    # ================== URL から、 原本 HTMLファイル、 比較用 HTMLファイル作成
    get_url = url
    response = requests.get(get_url, verify=False)
    #html_text = BeautifulSoup(response.text, 'html.parser')
    html_text = BeautifulSoup(response.text, 'lxml')

    # ファイル存在チェック
    if os.path.exists(DIR_PATH + file_name):  # python/test/back_up
        # === ファイルが存在していたら、比較用　ファイル作成
        File_Write(DIR_PATH_HIKAKU + file_name, html_text)  # ファイル書き込み関数
    else:
        # === ファイルが存在していなかったら、原本ファイル作成
        File_Write(DIR_PATH + file_name, html_text)  # ファイル書き込み関数


def File_Write(path_w, get_text):
    # ================== ファイル書き込み
    with open(path_w, mode='wb') as f:
        for item in get_text:
            f.write(item.encode('utf-8'))


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


class Send_Mail():

    def __init__(self, host, port, account, password, from_email, to_email):
        self.host = host
        self.port = port
        self.account = account
        self.password = password
        self.from_email = from_email
        self.to_email = to_email

    def Set_Smtp(self, host, port):
        if self.host != None and self.port != None:
            return smtplib.SMTP(self.host, self.port)
        else:
            return smtplib.SMTP(host, port)

    def Set_Account(self, account, password):

        if self.account != None and self.password != None:
            Account[0] = self.account
            Account[1] = self.password
            return Account
        else:
            Account = []
            Account[0] = account
            Account[1] = password
            return Account

    def Mail_from_to(self, from_email, to_email):

        if self.from_email != None and self.to_email != None:
            From_To = []
            From_To[0] = self.to_email
            From_To[1] = self.from_email
            return From_To
        else:
            From_To = []
            From_To[0] = to_email
            From_To[1] = from_email
            return From_To

    def Send_Mail_To(self):

        # MIMEの作成
        subject = "テストメール3"
        message = "テストメール3"
        msg = MIMEText(message, "html")
        msg["Subject"] = subject
        msg["To"] = self.to_email
        msg["From"] = self.from_email

        # メール送信処理
        # server = smtplib.SMTP("smtp.gmail.com", ポート)
        server = smtplib.SMTP(self.host, self.port)
      #  server = Send_obj.Set_Smtp(self.host, self.port)
        server.starttls()
        server.login(self.account, self.password)
        server.send_message(msg)

        server.quit()

        # ====== メール送信
        # server = smtplib.SMTP("SMTPサーバ", ポート番号)

        # デバッガ
        # server.set_debuglevel(True)
        # === 送受信先


def Send_Mail_Body():
    # === ファイルが違った場合のエラーメッセージ
    r_message = ''
    r_message = 'ファイル名:diff.html' + '\n'
    r_message += 'メッセージ内容:ソースが違っています。'
    return r_message


# ======================= 作業 Start ======================

# === ディレクトリ作成
Check_Dir(DIR_PATH)  # 原本 ディレクトリ
Check_Dir(DIR_PATH_HIKAKU)  # 比較用 ディレクトリ


# selenium での　chrome の実行ファイル　指定
driver = webdriver.Chrome(
    executable_path=r'C:\\chromedriver_win32\\chromedriver.exe')

driver.get("https://192.168.254.204/kdemo/index.php")

# === ＊＊＊＊＊＊＊＊＊＊＊＊　index.php

# ＊＊＊ スクレイピング　、　ログファイル作成
GET_Scraping_Requests(driver.current_url, 'index.txt')

# click イベント
btn_01 = driver.find_element(By.ID, "test_01_btn").click()
time.sleep(0.6)

# === view_list.php

print("カレントURL 2:::" + driver.current_url)


py_btn_02 = driver.find_element(By.ID, "py_btn_02").click()
time.sleep(0.6)

# === ＊＊＊＊＊＊＊＊＊＊＊＊ login.php

# ＊＊＊ スクレイピング　、　ログファイル作成
GET_Scraping_Requests(driver.current_url, 'login.txt')

user_id = driver.find_element(By.NAME, "user_id")  # name 属性取得
pass_word = driver.find_element(By.NAME, "password")  # name 属性取得

user_id.clear()
pass_word.clear()

user_id.send_keys("jimcom35")  # name 属性に値をセット
pass_word.send_keys("Jim357221")  # name 属性に値をセット

user_id.submit()  # form を submit する。

# time.sleep(0.6)

# =====================================================================================
# ================== view_list.php　、　「火葬タイプ」 「予約日」　指定　==================
# =====================================================================================

print('カレントURL:::' + driver.current_url)

# ＊＊＊ スクレイピング　、　ログファイル作成
GET_Scraping_Requests(driver.current_url, 'view_list.txt')

py_btn_02 = driver.find_element(By.ID, "py_btn_02").click()

# ====================================================
# ================ reserve_list.php ==================
# ====================================================
time.sleep(0.6)

GET_Scraping_Requests(driver.current_url, 'reserve_list.txt')

driver.execute_script("main.setModeAndSubmit('form1', 'view_list')")

time.sleep(0.6)

# =====================================================================================
# ================== view_list.php　、　「火葬タイプ」 「予約日」　指定　==================
# =====================================================================================

# 火葬タイプ選択  kasou_type
# radio_01 = driver.find_element(By.NAME, 'kasou_type')[0].click()
# radio_01 = driver.find_elements_by_css_selector('.k_type')
# driver.find_element(By.NAME, "kasou_type")[0].click()

# ラジオボタン ==　遺体(12歳以上)
driver.find_element(By.XPATH,
                    "//*[@id='form1']/table/tbody/tr[1]/td/span[2]/label[1]/input").click()

# ラジオボタン ==　死産児
# driver.find_element(
#    By.XPATH, "//*[@id='form1']/table/tbody/tr[1]/td/span[2]/label[3]/input").click()

time.sleep(5.0)

# ========== 日付け・時間  実行 ==========
Date_Obj = Date_To()
k_date = Date_Obj.Now_date()

g_date = Date_Obj.Date_cut(k_date)
# print(g_date)

# driver.execute_script("javascript:execCalendarLink('1','3','G001011014')")


# === 予約日　指定（ベタ打ち）
# driver.execute_script(
#    "javascript:main.set4KeyAndSubmit('form1', 'reserve_entry', 'YOYAKUBI', '22-11-14','WAKU_NO', '6', 'YOYAKU_TIME', '14:00', 'shiki_type', '0')")


# ========= 枠ナンバー ＆　時間　指定  ===========

t_time_0 = Date_Obj.Yoyaku_Time_idx(6, 0)  # 7
t_time_1 = Date_Obj.Yoyaku_Time_idx(6, 1)  # 例：15:00
# print(t_time_0 + ':::出力')
# print(t_time_1 + ':::出力')

# === 当日日付けを、10日プラスして、str に変えて s_data_add に格納
date_add = Date_Obj.Date_Add(10)
s_date_add = Date_Obj.Date_cut(date_add)
print('s_date_add:::' + s_date_add)

# ========= 枠ナンバー ＆　時間　指定 END  ===========


# === 予約日　指定 （変数　埋め込み）
driver.execute_script(
    "javascript:main.set4KeyAndSubmit('form1', 'reserve_entry', 'YOYAKUBI'," + "\'" + s_date_add + "\'" + ", 'WAKU_NO', " + "\'" + t_time_0 + "\'" + ", 'YOYAKU_TIME', " + "\'" + t_time_1 + "\'" + ", 'shiki_type', '0')")

# element = driver.find_element(By.LINK_TEXT, '5')
# print('リンクテキスト取得:::' + element)

time.sleep(1.0)


# ========== reserve_edit.php


# === フォームに値セット
Set_Name_Val('souke_name', '織田')  # 葬家名
Set_Name_Val('souke_kana', 'おだ')  # 葬家名（ふりがな）
Set_Name_Val('attendance', '33')  # 参列人数
Set_Name_Val('dead_kana01', 'おだ')  # 死亡者かな 姓
Set_Name_Val('dead_kana02', 'のぶひで')  # 死亡者かな 名
Set_Name_Val('dead_name01', '織田')  # 死亡者氏名 姓
Set_Name_Val('dead_name02', '信秀')  # 死亡者氏名  名

time.sleep(0.5)

GET_Scraping_Requests(driver.current_url, 'reserve_edit.txt')

# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
driver.execute_script("window.scrollTo(0, 1000);")

time.sleep(0.5)

Set_Name_Val('applicant_kana01', 'おだ')
Set_Name_Val('applicant_kana02', 'のぶなが')
Set_Name_Val('applicant_name01', '織田')
Set_Name_Val('applicant_name02', '信長')
Set_Name_Val('applicant_tel01', '000')
Set_Name_Val('applicant_tel02', '1111')
Set_Name_Val('applicant_tel03', '2222')
Set_Name_Val('applicant_tdkdet', '親子')

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# === javascript 実行 「予約を登録する」　ボタンを submit
driver.execute_script(
    "main.setModeAndSubmit('form1', 'entry_confirm')")

time.sleep(1.0)

# =====================================================================================
# ================== reserve_confirm.php　==================
# =====================================================================================

GET_Scraping_Requests(driver.current_url, 'reserve_confirm.txt')

time.sleep(0.5)

# ===　＊＊＊＊＊＊＊＊＊＊　Chrome Driver 終了 & chrome終了　＊＊＊＊＊＊＊＊＊＊
driver.quit()

# === 予約 OK ボタン　submit
# driver.execute_script(
#    "main.setModeAndSubmit('form1', 'entry_execute')")

# ===
