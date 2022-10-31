import requests
from bs4 import BeautifulSoup, BeautifulStoneSoup

from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Selenium用オプション
#op = Options()
# op.add_argument('--ignore-certificate-errors')
# op.add_argument('--ignore-ssl-errors')

# driver = webdriver.Chrome(
# executable_path=r'C:\\chromedriver_win32\\chromedriver.exe', chrome_options=op)


def GET_Scraping_Requests(url):
    get_url = url
    response = requests.get(get_url, verify=False)
    print(response)


driver = webdriver.Chrome(
    executable_path=r'C:\\chromedriver_win32\\chromedriver.exe')

GET_Scraping_Requests("https://192.168.254.204/kdemo/index.php")


# driver.get("https://192.168.254.204/kdemo/login.php")
driver.get("https://192.168.254.204/kdemo/index.php")
# click イベント
btn_01 = driver.find_element(By.ID, "test_01_btn").click()

# btn_01.click()
time.sleep(1.5)


print(driver.current_url)

# ==============================================================
# ===================== transactionid 取得 =====================
# ==============================================================
url_str = driver.current_url
target = '?transactionid='
idx = url_str.find(target)

t_id = url_str[idx + len(target):]

print(t_id)  # transactionid　出力
# ===============================================================
# ===================== transactionid 取得 END ==================
# ===============================================================


url = "https://192.168.254.204/kdemo/login.php?transactionid=" + t_id
session = requests.session()
response = session.get(url, verify=False)
bs = BeautifulSoup(response.text, 'html.parser')

# クッキーとトークンを取得

# authenticity = bs.find(attrs={'name': '_token'}).get('value')
cookie = response.cookies

info = {
    #    "_token": authenticity,
    "transactionid": t_id,
    "an_user": "",
    "an_password": ""
}

# URLを叩き、htmlを表示
res = session.post(url, data=info, cookies=cookie)
print(res.text)
