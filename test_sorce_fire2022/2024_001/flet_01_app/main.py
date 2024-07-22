import flet as ft
import datetime


def main(page: ft.page):
    page.title = "ファイル改ざん検知 アプリ"

    page.window_width = 460  # 幅
    page.window_height = 620  # 高さ
    page.window_resizable = False  # ウィンドウサイズ変更可否

    url = ft.TextField(label="対象URL")  # ラベル
    start_btn = ft.ElevatedButton("開始", icon="gavel")  # ボタン

    page.add(url, start_btn)


ft.app(target=main)
