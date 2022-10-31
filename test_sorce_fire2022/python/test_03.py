import requests
from bs4 import BeautifulSoup, BeautifulStoneSoup


# ログインページ URL から BeautifulSoup オブジェクト作成

# url = "http://xs810378.xsrv.jp/JimYoyaku_Demo/yoyaku/login"
url = "https://192.168.254.204/kdemo/login.php"
session = requests.session()
response = session.get(url, verify=False)
bs = BeautifulSoup(response.text, 'html.parser')

# クッキーとトークンを取得

# authenticity = bs.find(attrs={'name': '_token'}).get('value')
cookie = response.cookies

info = {
    #    "_token": authenticity,
    "an_user": "",
    "an_password": ""
}

# URLを叩き、htmlを表示
res = session.post(url, data=info, cookies=cookie)
print(res.text)
