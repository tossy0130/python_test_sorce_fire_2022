import flet as ft
import datetime

import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import time
from selenium.webdriver.common.by import By

# 外部ファイルから関数をインポート
from lib.html_cut import HTML_CUT  # HTML 加工用
from lib.conf import Config_Setting  # 設定情報
from lib.file_related import File_related  # ファイル操作関係
from lib.scraping import Scraping_Requests  # スクレイピング、クローリング用
from lib.date_to import Date_to  # 日付系のクラス


def main(page: ft.page):
    page.title = "ファイル改ざん検知 アプリ"

    page.window_width = 460  # 幅
    page.window_height = 620  # 高さ
    page.window_resizable = False  # ウィンドウサイズ変更可否

    page.window_top = 200  # 位置(TOP)
    page.window_left = 760  # 位置(LEFT)

    # 日時表示 ラベル
    time_view = Date_to.Get_formatted_date()
    time_label = ft.Text(value=time_view,
                         size=14)

    # URL 表示ラベル
    url_label = ft.Text(value="■ 対象URL")
    url_label_val = ft.Text(size=16,
                            color=ft.colors.WHITE,
                            value=Config_Setting.READ_URL)

    # 状態判別 スイッチ
    c1 = ft.Switch(
        label=Config_Setting.SOURCE_01,  # ソース名 01
        value=True,
    )

    c2 = ft.Switch(
        label=Config_Setting.SOURCE_02,  # ソース名 01
        value=True,
    )

    c3 = ft.Switch(
        label=Config_Setting.SOURCE_03,  # ソース名 01
        value=True,
    )

    c4 = ft.Switch(
        label=Config_Setting.SOURCE_04,  # ソース名 01
        value=True,
    )

    # ラベルを四角で囲むコンテナ
    container_01 = ft.Container(
        content=url_label_val,
        margin=10,
        padding=5,
        alignment=ft.alignment.center,
        bgcolor=ft.colors.BLACK54,
        width=400,
        height=80,
        border_radius=10,
    )

    def start_btn_click(e):
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
        scraper = Scraping_Requests()
        scraper.GET_Scraping_Requests(
            'index.txt', driver.page_source, original_dir, comparison_dir)

        # index.php => ログイン click イベント
        btn_01 = driver.find_element(
            By.XPATH, "//*[@id='form1']/div[1]/ul/li[2]/a").click()
        time.sleep(0.6)

        # ============================
        # === view_list.php
        # ============================

        py_btn_02 = driver.find_element(By.ID, "py_btn_02").click()
        time.sleep(0.6)

        # ============================
        # === login.php
        # ============================
        scraper.GET_Scraping_Requests(
            'login.txt', driver.page_source, original_dir, comparison_dir)

        user_id = driver.find_element(By.NAME, "user_id")  # name 属性取得
        pass_word = driver.find_element(By.NAME, "password")  # name 属性取得

        user_id.clear()
        pass_word.clear()

        user_id.send_keys("jimcom35")  # name 属性に値をセット
        pass_word.send_keys("jim357221")  # name 属性に値をセット

        # form を submit する。
        user_id.submit()

        # =====================================================================================
        # ================== view_list.php　、　「火葬タイプ」 「予約日」　指定　==================
        # =====================================================================================

        time.sleep(2.6)

        scraper.GET_Scraping_Requests(
            'view_list.txt', driver.page_source, original_dir, comparison_dir)

        py_btn_02 = driver.find_element(By.ID, "py_btn_02").click()

        # ====================================================
        # ================ reserve_list.php ==================
        # ====================================================

        time.sleep(4.6)

        scraper.GET_Scraping_Requests(
            'reserve_list.txt', driver.page_source, original_dir, comparison_dir)

        time.sleep(1.0)

        driver.execute_script("main.setModeAndSubmit('form1', 'view_list')")

        # =====================================================================================
        # ================== view_list.php　、　「火葬タイプ」 「予約日」　指定　==================
        # =====================================================================================

        # ラジオボタン ==　遺体(12歳以上)
        driver.find_element(By.XPATH,
                            "//*[@id='form1']/table/tbody/tr[1]/td/span[2]/label[1]/input").click()

        time.sleep(1.0)

        # ========== 日付け・時間  実行 ==========
        Date_Obj = Date_to()
        k_date = Date_Obj.Now_date()

        g_date = Date_Obj.Date_cut(k_date)

        # ========= 枠ナンバー ＆　時間　指定  ===========
        # パラメーターで 予約枠の時間と、 枠番号を指定
        t_time_0 = Date_Obj.Yoyaku_Time_idx(1, 0)  # 7
        t_time_1 = Date_Obj.Yoyaku_Time_idx(1, 1)  # 例：15:00

        # === 当日日付けを、10日プラスして、str に変えて s_data_add に格納
        # 日付指定　　
        date_add = Date_Obj.Date_Add(10)  # ********* パラメータ日後 *********
        s_date_add = Date_Obj.Date_cut(date_add)
        print('s_date_add:::' + s_date_add)

        # ================================================================
        # ========= 枠ナンバー ＆　時間　指定 END  ===========
        # ================================================================

        # === 予約日　指定 （変数　埋め込み）
        driver.execute_script(
            "javascript:main.set4KeyAndSubmit('form1', 'reserve_entry', 'YOYAKUBI'," + "\'" + s_date_add + "\'" + ", 'WAKU_NO', " + "\'" + t_time_0 + "\'" + ", 'YOYAKU_TIME', " + "\'" + t_time_1 + "\'" + ", 'shiki_type', '0')")

        time.sleep(1.0)

        # ====================================================
        # ================ reserve_edit.php ==================
        # ====================================================

        scraper.GET_Scraping_Requests(
            'reserve_edit.txt', driver.page_source, original_dir, comparison_dir)

        # === フォームに値セット
        Scraping_Requests.Set_Name_Val('souke_name', '織田', driver)  # 葬家名
        Scraping_Requests.Set_Name_Val('souke_kana', 'おだ', driver)  # 葬家名（ふりがな）
        Scraping_Requests.Set_Name_Val('attendance', '33', driver)  # 参列人数
        Scraping_Requests.Set_Name_Val('dead_kana01', 'おだ', driver)  # 死亡者かな 姓
        Scraping_Requests.Set_Name_Val(
            'dead_kana02', 'のぶひで', driver)  # 死亡者かな 名
        Scraping_Requests.Set_Name_Val('dead_name01', '織田', driver)  # 死亡者氏名 姓
        Scraping_Requests.Set_Name_Val('dead_name02', '信秀', driver)  # 死亡者氏名  名

        time.sleep(1.0)

        driver.execute_script("window.scrollTo(0, 1000);")

        time.sleep(1.0)

        Scraping_Requests.Set_Name_Val('applicant_kana01', 'おだ', driver)
        Scraping_Requests.Set_Name_Val('applicant_kana02', 'のぶなが', driver)
        Scraping_Requests.Set_Name_Val('applicant_name01', '織田', driver)
        Scraping_Requests.Set_Name_Val('applicant_name02', '信長', driver)
        Scraping_Requests.Set_Name_Val('applicant_tel01', '000', driver)
        Scraping_Requests.Set_Name_Val('applicant_tel02', '1111', driver)
        Scraping_Requests.Set_Name_Val('applicant_tel03', '2222', driver)
        Scraping_Requests.Set_Name_Val('applicant_tdkdet', '親子', driver)

        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")

        # === javascript 実行 「予約を登録する」　ボタンを submit
        driver.execute_script(
            "main.setModeAndSubmit('form1', 'entry_confirm')")

        time.sleep(1.0)

        # ====================================================
        # ================ reserve_confirm.php ==================
        # ====================================================

        scraper.GET_Scraping_Requests(
            'reserve_confirm.txt', driver.page_source, original_dir, comparison_dir)

        time.sleep(1.0)

        # ===　＊＊＊＊＊＊＊＊＊＊　Chrome Driver 終了 & chrome終了　＊＊＊＊＊＊＊＊＊＊
        driver.quit()  # chromeを閉じる

    # ================ コンポーネント追加
    page.add(time_label,
             url_label,
             container_01,
             c1,
             c2,
             c3,
             c4,
             ft.ElevatedButton("開始", icon="gavel", on_click=start_btn_click)
             )


ft.app(target=main)
