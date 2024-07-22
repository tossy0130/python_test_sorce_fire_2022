import requests
import os
from bs4 import BeautifulSoup
from selenium import webdriver
from lib.file_related import File_related


class Scraping_Requests(File_related):
    def GET_Scraping_Requests(self, file_name, html_text, dir_path, dir_path_hikaku):

        try:
            if os.path.exists(dir_path + file_name):
                # ファイルが存在していたら、比較用ファイルを作成
                self.File_Write(dir_path_hikaku + file_name, html_text)
                print("GET_Scraping_Requests:::比較用 ファイル作成 完了" + "\n")

                print("file_name:::" + file_name)
                print("html_text:::" + html_text)
                print("dir_path_hikaku:::" + dir_path_hikaku + "\n")
            else:
                # ファイルが存在してなかったら、原本ファイルを作成
                self.File_Write(dir_path + file_name, html_text)
                print("GET_Scraping_Requests:::原本 ファイル作成 完了" + "\n")

                print("file_name:::" + file_name)
                print("html_text:::" + html_text)
                print("dir_path:::" + dir_path + "\n")
        except Exception as e:
            print(f"ファイル処理中にエラーが発生しました:{e}")
