import requests
from selenium import webdriver
from bs4 import BeautifulSoup


# =================================================================
# ===================== chromeドライバーの読み込み ==================
# =================================================================
driver = webdriver.Chrome()

html = driver.page_source
# print("html 値:::" + html + "\n\n")

# URL から HTMLを取得
# verify=FalseはSSL証明書の検証を無効にする
response = requests.get(driver.current_url, verify=False)

# HTMLをファイルに保存
with open('dowwnload_page.html', 'w', encoding='utf-8') as file:
    file.write(response.text)

# ファイルからHTMLを読み込み、html_contentに保存
with open('dowwnload_page.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# HTML を表示（確認用）
print(html_content)
