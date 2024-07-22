import requests
from selenium import webdriver
from bs4 import BeautifulSoup

# 外部ファイルから関数をインポート
from lib.html_cut import HTML_CUT  # HTML 加工用
from lib.conf import Config_Setting  # 設定情報
from lib.file_related import File_related  # ファイル操作関係
from lib.scraping import Scraping_Requests  # スクレイピング、クローリング用


def main():
    # =============== 初期設定
    log_dir = Config_Setting.LOG_DIR  # ログ用ディレクトリ 作成
    File_related.Check_Dir(log_dir)

    original_dir = Config_Setting.ORIGINAL_DIR  # 原本用 ディレクトリ 作成
    File_related.Check_Dir(original_dir)

    comparison_dir = Config_Setting.COMPARISON  # 比較用 ディレクトリ 作成
    File_related.Check_Dir(comparison_dir)

    # =================================================================
    # ===================== chromeドライバーの読み込み ==================
    # =================================================================
    # 読み込み対象　URL
    url = Config_Setting.READ_URL

    driver = webdriver.Chrome()
    driver.get(url)

    # Scraping_Requests クラスオブジェクト生成

   # html_text = driver.page_source  # selenium

    scraper = Scraping_Requests()
    scraper.GET_Scraping_Requests(
        'index.txt', driver.page_source, original_dir, comparison_dir)


if __name__ == "__main__":
    main()
