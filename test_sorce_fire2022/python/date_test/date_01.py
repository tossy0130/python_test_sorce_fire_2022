import datetime


class Date_To():
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

    # === 当日取得 ::: 2022-11-04 14:26:56.878021
    def Now_date(self):
        dt_now = datetime.datetime.now()
        return dt_now

    # === 日付 ::: フォーマット 22-11-04
    def Date_cut(self, t_date):
        now_date = t_date
        n_now_date = now_date.strftime("%y-%m-%d")
        return n_now_date

    # === index に応じた time_num の時間を出力
    def Yoyaku_Time_idx(self, idx, idx_02):
        return self.time_num[idx][idx_02]


# === 実行
Date_Obj = Date_To()
k_date = Date_Obj.Now_date()

g_date = Date_Obj.Date_cut(k_date)
print(g_date)

# ========= 枠ナンバー ＆　時間　出力 ===========
t_time_0 = Date_Obj.Yoyaku_Time_idx(4, 0)  # 例：5
print(t_time_0 + ':::出力')
t_time_1 = Date_Obj.Yoyaku_Time_idx(4, 1)  # 例：13:00
print(t_time_1 + ':::出力')
