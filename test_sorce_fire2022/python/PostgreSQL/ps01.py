import psycopg2
from psycopg2 import Error
from psycopg2.extras import DictCursor
import pandas as pd


try:
    # === 接続
    connector = psycopg2.connect('postgresql://{user}:{password}@{host}:{port}/{dbname}'.format(
        user="ユーザー",  # ユーザ
        password="パス",  # パスワード
        host="localhost",  # ホスト名
        port="5432",  # ポート
        dbname="postgres"))  # データベース名

    # ========= SQL
    cursor = connector.cursor()
    cursor.execute("SELECT * FROM goals")

    # ====== １件分　だけ抽出
    row = cursor.fetchone()
    print(row)

    # ====== 全件まとめて取得
    f_all = cursor.fetchall()
    print(f_all)

    for f_val in f_all:
        print(f_val)

    # ====== 辞書型で取得
    cursor_02 = connector.cursor(cursor_factory=DictCursor)


except(Exception, Error) as error:
    print("PostgreSQLへの接続時のエラーが発生しました", error)

finally:
    cursor.close()
    connector.close()
