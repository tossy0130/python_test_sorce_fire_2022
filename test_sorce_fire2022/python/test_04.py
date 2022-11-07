import requests
from bs4 import BeautifulSoup, BeautifulStoneSoup

from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import os


# 社内 環境
# Selenium用オプション
#op = Options()
# op.add_argument('--ignore-certificate-errors')
# op.add_argument('--ignore-ssl-errors')

# driver = webdriver.Chrome(
# executable_path=r'C:\\chromedriver_win32\\chromedriver.exe', chrome_options=op)


def GET_Scraping_Requests(url, file_name):
    # ================== URL から、 原本 HTMLファイル、 比較用 HTMLファイル作成
    get_url = url
    response = requests.get(get_url, verify=False)
    #html_text = BeautifulSoup(response.text, 'html.parser')
    html_text = BeautifulSoup(response.text, 'lxml')

    File_Write('python/back_up/' + file_name, html_text)  # ファイル書き込み関数

    # ファイル存在チェック
    if os.path.exists('python/back_up/' + file_name):
        # === ファイルが存在していたら、比較用　ファイル作成
        File_Write('python/back_up_02/' + file_name, html_text)  # ファイル書き込み関数
    else:
        # === ファイルが存在していなかったら、原本ファイル作成
        File_Write('python/back_up/' + file_name, html_text)  # ファイル書き込み関数


def File_Write(path_w, get_text):
    # ================== ファイル書き込み
    with open(path_w, mode='wb') as f:
        for item in get_text:
            f.write(item.encode('utf-8'))


def File_Check():
    # ================== ディレクトリ作成
    path = 'python/back_up'

    try:
        if (os.path.isdir(path)):  # フォルダが存在していた場合
            pass
        else:
            os.mkdir('python/back_up')  # フォルダが存在していなかったら作成
    except FileExistsError:
        print('file_error')

# ===================


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


# ファイルチェック実行
File_Check()
Check_Dir('python/back_up_02')

driver = webdriver.Chrome(
    executable_path=r'C:\\chromedriver_win32\\chromedriver.exe')

# driver.get("https://192.168.254.204/kdemo/login.php")
driver.get("https://192.168.254.204/kdemo/index.php")

print('============ driver index.php 取得  ============')
print(driver.page_source)

# === 実行
get_url = "https://192.168.254.204/kdemo/index.php"
GET_Scraping_Requests(get_url, 'index.txt')


# click イベント
btn_01 = driver.find_element(By.ID, "test_01_btn").click()

# btn_01.click()
time.sleep(0.6)


print("カレントURL:::" + driver.current_url)

# view_list.php　（ログイン前）
# ==============================================================
# ===================== transactionid 取得 =====================
# ==============================================================
url_str = driver.current_url
target = '?transactionid='
idx = url_str.find(target)

t_id = url_str[idx + len(target):]

# === 実行
GET_Scraping_Requests(url_str, 'view_list.txt')

py_btn_02 = driver.find_element(By.ID, "py_btn_02").click()
time.sleep(0.6)


# ===============================================================
# ===================== transactionid 取得 END ==================
# ===============================================================

# login.php
url = "https://192.168.254.204/kdemo/login.php?transactionid=" + t_id
login_url = driver.current_url

# === 実行
GET_Scraping_Requests("https://192.168.254.204/kdemo/view_list.php?transactionid=" +
                      t_id, 'login.txt')

user_id = driver.find_element(By.NAME, "user_id")  # name 属性取得
pass_word = driver.find_element(By.NAME, "password")  # name 属性取得

# driver.find_element 単数
# driver.find_elements 複数

user_id.clear()
pass_word.clear()

user_id.send_keys("jimcom35")  # name 属性に値をセット
pass_word.send_keys("Jim357221")  # name 属性に値をセット

user_id.submit()  # form を submit する。

time.sleep(0.6)

# ================================================================
# ========= ログイン済み　view_list.php =========  ここから
# ================================================================
view_list_in_url = driver.current_url
print("カレントURL:::" + view_list_in_url)
print("カレントURL driver:::" + driver.current_url)
GET_Scraping_Requests(view_list_in_url, 'view_list.txt')


# =========== view_list.php を txt ファイルへ格納

response_view = requests.get(view_list_in_url, verify=False)
#view_php_text = BeautifulSoup(response_view.text, 'lxml')
view_php_text = BeautifulSoup(response_view.text, 'html.parser')
print(view_php_text)

# ================ とりあえず ファイル出力テスト =================
if not os.path.isfile('test.txt'):
    with open('test.txt', mode='wb') as f:
        for val in view_php_text:
            f.write(val.encode('utf-8'))
            print("============= test.txt 作成 OK if =============")

else:
    with open('test.txt', mode='wb') as f:
        for val in view_php_text:
            f.write(val.encode('utf-8'))
            print("============= test.txt 作成 OK else =============")
