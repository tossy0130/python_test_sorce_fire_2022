import time
import datetime


class Date_to():
    # ============ 日時・時刻　クラス　============
    # 予約時間　格納用
    def __init__(self):
        self.time_num = [
            ['1', '9:00'],
            ['2', '10:00'],
            ['3', '11:00'],
            ['4', '12:00'],
            ['5', '13:00'],
            ['6', '14:00'],
            ['7', '15:00']
        ]

        self.dt_now = ""

    # === 当日取得 ::: 2022-11-04 14:26:56.878021
    def Now_date(self):
        self.dt_now = datetime.datetime.now()
        return self.dt_now

    # === 日付 ::: フォーマット 22-11-04
    def Date_cut(self, t_date):
        now_date = t_date
        n_now_date = now_date.strftime("%y-%m-%d")
        return n_now_date

    # === index に応じた time_num の時間を出力
    def Yoyaku_Time_idx(self, idx, idx_02):
        return self.time_num[idx][idx_02]

    # === 当日から num　を加算した値を返す
    def Date_Add(self, num):
      #  self.dt_now = datetime.datetime.now()
        date_add = self.dt_now + datetime.timedelta(days=num)
        return date_add
        # Date_To ****** END ********

    @staticmethod
    def Get_formatted_date():
        """
        flet に表示用の日付関数
        """
        # 現在の日時
        today = datetime.date.today()

        # 日付フォーマット
        formatted_date = today.strftime(f"%Y年%m月%d日（%a）")

        # 日本語の曜日に変換
        weekdays = {"Mon": "月", "Tue": "火", "Wed": "水",
                    "Thu": "木", "Fri": "金", "Sat": "土", "Sun": "日"}

        weekday_jp = weekdays[today.strftime("%a")]

        return formatted_date.replace(today.strftime("%a"), weekday_jp)
