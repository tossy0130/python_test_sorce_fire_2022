from distutils import bcppcompiler
import tkinter
from tkinter import messagebox
import requests
from bs4 import BeautifulSoup


# ============== tkinter ゾーン =============

def Url_get():
    # テキストボックスの URL を取得
    GET_URL = textBox.get()

    # ============ スクレイピング ============
   # url = "http://www.jimnet.co.jp/"
    r = requests.get(GET_URL)

    soup = BeautifulSoup(r.content, 'html.parser')
    # soup = BeautifulSoup(r.text, 'html.parser')

    get_textBox.insert(tkinter.END, soup)
    # print(soup)


root = tkinter.Tk()

# アプリの画面設定
root.geometry(
    "1200x600"  # アプリ画面のサイズ
)

# ボタン作成
btn = tkinter.Button(root, text="取得", width="14",  command=Url_get)
# 配置
btn.place(x=150, y=50)

btn_02 = tkinter.Button(root, text="解析", width="14")
btn_02.place(x=400, y=50)

# テキストボックスWidget１を生成
textBox = tkinter.Entry(root)
textBox.place(x=300, y=120, relheight=0.05,
              relwidth=0.5, anchor=tkinter.W)

# URL から取得した　情報
get_textBox = tkinter.Text(root)
get_textBox.place(x=100, y=350, relheight=0.7,
                  relwidth=0.6, anchor=tkinter.W)

# ==============


root.mainloop()
