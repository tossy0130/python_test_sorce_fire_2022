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
    get_url = url
    response = requests.get(get_url, verify=False)
    #html_text = BeautifulSoup(response.text, 'html.parser')
    html_text = BeautifulSoup(response.text, 'lxml')

    # ファイル存在チェック
    if os.path.exists('python/back_up/' + file_name):
        # === function 実行 ===
        File_Write('python/back_up/' + file_name, html_text)  # ファイル書き込み関数
    else:
        # ファイルが無かった場合は作成する
        path = 'python/back_up/' + file_name
        f = open(path, 'w')
        f.write('')
        f.close()

# ================== ファイル書き込み


def File_Write(path_w, get_text):
    with open(path_w, mode='wb') as f:
        for item in get_text:
            f.write(item.encode('utf-8'))


# ================== フォルダ作成
def File_Check():
    path = 'python/back_up'

    try:
        if (os.path.isdir(path)):  # フォルダが存在していた場合
            pass
        else:
            os.mkdir('python/back_up')  # フォルダが存在していなかったら作成
    except FileExistsError:
        print('file_error')

# ===================


# ファイルチェック実行
File_Check()

driver = webdriver.Chrome(
    executable_path=r'C:\\chromedriver_win32\\chromedriver.exe')

# driver.get("https://192.168.254.204/kdemo/login.php")
driver.get("https://192.168.254.204/kdemo/index.php")

# === 実行
get_url = "https://192.168.254.204/kdemo/index.php"
GET_Scraping_Requests(get_url, 'index.txt')


# click イベント
btn_01 = driver.find_element(By.ID, "test_01_btn").click()

# btn_01.click()
time.sleep(1.0)


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
time.sleep(1.0)


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

time.sleep(1.0)

# ========= ログイン済み　view_list.php =========
view_list_in_url = driver.current_url
print("カレントURL:::" + view_list_in_url)
print("カレントURL driver:::" + driver.current_url)
GET_Scraping_Requests(view_list_in_url, 'view_list.txt')
