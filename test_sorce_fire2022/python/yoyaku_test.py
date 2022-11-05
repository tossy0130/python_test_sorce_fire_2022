import datetime

import requests
from bs4 import BeautifulSoup, BeautifulStoneSoup

from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import os

# Date_To ****** START ********


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

    def Date_Add(self, num):
        date_add = self.dt_now + datetime.timedelta(day=num)
        return date_add
        # Date_To ****** END ********


def Set_Name_Val(name, set_val):
    tmp_name = driver.find_element(By.NAME, name)  # name 属性取得
    tmp_name.clear()
    tmp_name.send_keys(set_val)  # name 属性に値をセット

    # === 実行
Date_Obj = Date_To()
k_date = Date_Obj.Now_date()

g_date = Date_Obj.Date_cut(k_date)
print(g_date)


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

# driver.execute_script("javascript:execCalendarLink('1','3','G001011014')")

# driver.execute_script(
#    "javascript:main.set4KeyAndSubmit('form1', 'reserve_entry', 'YOYAKUBI', '22-11-14','WAKU_NO', '6', 'YOYAKU_TIME', '14:00', 'shiki_type', '0')")


# ========= 枠ナンバー ＆　時間　指定  ===========
t_time_0 = Date_Obj.Yoyaku_Time_idx(6, 0)  # 7
t_time_1 = Date_Obj.Yoyaku_Time_idx(6, 1)  # 例：15:00
print(t_time_0 + ':::出力')
print(t_time_1 + ':::出力')

date_add = Date_Obj.Date_Add(10)
print(date_add)

driver.execute_script(
    "javascript:main.set4KeyAndSubmit('form1', 'reserve_entry', 'YOYAKUBI'," + "\'" + date_add + "\'" + ", 'WAKU_NO', " + "\'" + t_time_0 + "\'" + ", 'YOYAKU_TIME', " + "\'" + t_time_1 + "\'" + ", 'shiki_type', '0')")

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

driver.execute_script(
    "main.setModeAndSubmit('form1', 'entry_confirm')")

time.sleep(2.0)
