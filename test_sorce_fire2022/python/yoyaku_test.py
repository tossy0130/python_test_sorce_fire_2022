import datetime

import requests
from bs4 import BeautifulSoup, BeautifulStoneSoup

from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import os


class Date_To():
    # ============ 日時・時刻　クラス　============
    # 予約時間　格納用
    def __init__(self):
        self.time_num = {'1': '9:00', '2': '10:00', '3': '11:00',
                         '4': '12:00', '5': '13:00', '6': '14:00', '7': '15:00'}

    # === 当日取得 ::: 2022-11-04 14:26:56.878021
    def Now_date(self):
        dt_now = datetime.datetime.now()
        return dt_now

    # === 日付 ::: フォーマット 22-11-04
    def Date_cut(self, t_date):
        now_date = t_date
        n_now_date = now_date.strftime("%y-%m-%d")
        return n_now_date

    # === index に応じた time_num の時間を出力
    def Yoyaku_Time_idx(self, idx):
        return self.time_num[idx]


driver = webdriver.Chrome(
    executable_path=r'C:\\chromedriver_win32\\chromedriver.exe')

driver.get("https://192.168.254.204/kdemo/index.php")

# === index.php
# click イベント
btn_01 = driver.find_element(By.ID, "test_01_btn").click()
time.sleep(0.6)

print("カレントURL:::" + driver.current_url)

# === view_list.php
py_btn_02 = driver.find_element(By.ID, "py_btn_02").click()
time.sleep(0.6)

# === login.php
user_id = driver.find_element(By.NAME, "user_id")  # name 属性取得
pass_word = driver.find_element(By.NAME, "password")  # name 属性取得

user_id.clear()
pass_word.clear()

user_id.send_keys("jimcom35")  # name 属性に値をセット
pass_word.send_keys("Jim357221")  # name 属性に値をセット

user_id.submit()  # form を submit する。

# time.sleep(0.6)

# === view_list.php
print('カレントURL:::' + driver.current_url)

# 火葬タイプ選択  kasou_type
# radio_01 = driver.find_element(By.NAME, 'kasou_type')[0].click()
# radio_01 = driver.find_elements_by_css_selector('.k_type')
# driver.find_element(By.NAME, "kasou_type")[0].click()
driver.find_element(By.XPATH,
                    "//*[@id='form1']/table/tbody/tr[1]/td/span[2]/label[1]/input").click()

time.sleep(5.0)

# ========== 日付け・時間  実行 ==========
Date_Obj = Date_To()
k_date = Date_Obj.Now_date()

g_date = Date_Obj.Date_cut(k_date)
print(g_date)

t_time = Date_Obj.Yoyaku_Time_idx(3)
print(t_time + ':::出力')

# driver.execute_script("javascript:execCalendarLink('1','3','G001011014')")

# driver.execute_script(
#    "javascript:main.set4KeyAndSubmit('form1', 'reserve_entry', 'YOYAKUBI', '22-11-14','WAKU_NO', '6', 'YOYAKU_TIME', '14:00', 'shiki_type', '0')")

# driver.execute_script(
#    "javascript:main.set4KeyAndSubmit('form1', 'reserve_entry', 'YOYAKUBI', '22-11-14','WAKU_NO', '6', 'YOYAKU_TIME'," + "\'" + t_time + "\'" + ", 'shiki_type', '0')")

time.sleep(3.0)

# element = driver.find_element(By.LINK_TEXT, '5')

# print('リンクテキスト取得:::' + element)
