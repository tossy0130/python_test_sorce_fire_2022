import requests
from selenium import webdriver
from bs4 import BeautifulSoup

# ================================================================
# =========================== HTML 削除クラス =====================
# ================================================================


class HTML_CUT():

    def __init__(self):

        self.cut_url = ""
        self.test_print = ""

    # ============== th タグ内の文字列 削除
    def HTML_TH_CUT(self):

        soup = BeautifulSoup(self.url, 'html.parser')
        # <th> タグを全て取得
        th_tags = soup.find_all('th')
        # <th> タグ内の文字列を出力
        for th_val in th_tags:
            print("val:::" + th_val + "\n")

    #
    def Test_Print(self):
        self.test_print = "テスト OK"
        print(self.test_print)
