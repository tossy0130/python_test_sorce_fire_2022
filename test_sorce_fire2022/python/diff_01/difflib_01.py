from enum import Flag
import os
import difflib

from smtplib import SMTP

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from email.utils import formatdate

from email.mime.text import MIMEText  # MIME 形式データ用
from email.utils import formatdate
import smtplib


# ================================= メール送信 ===================================
class Send_Mail():

    def __init__(self, host, port, account, password, from_email, to_email):
        self.host = host  # ホスト
        self.port = port  # ポート
        self.account = account  # アカウント
        self.password = password  # パスワード
        self.from_email = from_email  # メール送信元
        self.to_email = to_email  # メール送信先

    def Set_Smtp(self, host, port):
        if self.host != None and self.port != None:
            return smtplib.SMTP(self.host, self.port)
        else:
            return smtplib.SMTP(host, port)

    def Set_Account(self, account, password):

        if self.account != None and self.password != None:
            Account[0] = self.account
            Account[1] = self.password
            return Account
        else:
            Account = []
            Account[0] = account
            Account[1] = password
            return Account

    def Mail_from_to(self, from_email, to_email):

        if self.from_email != None and self.to_email != None:
            From_To = []
            From_To[0] = self.to_email
            From_To[1] = self.from_email
            return From_To
        else:
            From_To = []
            From_To[0] = to_email
            From_To[1] = from_email
            return From_To

    def Send_Mail_To(self):

        # MIMEの作成
        subject = "title:ソースを確認してください。"
        message = Send_Mail_Body()
        msg = MIMEText(message, "html")
        msg["Subject"] = subject
        msg["To"] = self.to_email
        msg["From"] = self.from_email

        # メール送信処理
        # server = smtplib.SMTP("smtp.gmail.com", ポート)
        server = smtplib.SMTP(self.host, self.port)
        #  server = Send_obj.Set_Smtp(self.host, self.port)
        server.starttls()
        server.login(self.account, self.password)
        server.send_message(msg)

        server.quit()


def Send_Mail_Body():
    # === ファイルが違った場合のエラーメッセージ
    r_message = ''
    r_message = 'ファイル名:diff.html' + '\n'
    r_message += 'メッセージ内容:ソースが違っています。'
    return r_message

    # ====== メール送信
    # server = smtplib.SMTP("SMTPサーバ", ポート番号)

    # デバッガ
    # server.set_debuglevel(True)


class Diff_File():
    def __init__(self, path_01, path_02, file_01, file_02):
        self.path_01 = path_01
        self.path_02 = path_02
        self.file_01 = file_01
        self.file_02 = file_02

    def Diff_HTML(self, output_dir_path, output_file_name):

        diff = difflib.HtmlDiff()
        output_file = output_file_name
        output_path = os.path.join(output_dir_path, output_file)


# ===================================================================================
# ================================= メール送信 END ===================================
# ===================================================================================
# ===================================================================================
# ================================= ソース比較 =======================================
# ===================================================================================
dir_path = r'D:\\Python_ソース比較_2022\\test_sorce_fire2022\\python\\back_up\\'

# 比較用　ファイル
file1_name = 'index.txt'
file2_name = 'index_test.txt'

# パスと、ファイル名　結合
file1_p = os.path.join(dir_path, file1_name)
file2_p = os.path.join(dir_path, file2_name)

file1 = open(file1_p, 'r', encoding="utf-8_sig")
file2 = open(file2_p, 'r', encoding="utf-8_sig")
# file1 = open(file1_p, 'r', encoding="sjis")
# file2 = open(file2_p, 'r', encoding="sjis")

# ======================  HtmlDiff() =======================

diff = difflib.HtmlDiff()

output_file = 'diff.html'
output_path = os.path.join(dir_path, output_file)

# ファイル書き込み
output_create = open(output_path, 'w', encoding="utf-8")
output_create.writelines(diff.make_file(file1, file2))

file1.close()
file2.close()

output_create.close()

# ====================== 差分のみの抽出  Differ() =======================

file11 = open(file1_p, 'r', encoding="utf-8_sig")
file22 = open(file2_p, 'r', encoding="utf-8_sig")
diff_02 = difflib.Differ()

output_diff02 = diff_02.compare(file11.readlines(), file22.readlines())

# === ファイルを比較して、違ったら False , 同じだったら True
Source_Flg = True
for data_02 in output_diff02:

    if data_02[0:1] in ['+', '-']:
        print(data_02)
        print('違いあり')
        Source_Flg = False
    else:
        print('ソース違いなし')

if Source_Flg:
    print('ソースOK')
else:
    # ======　ソースが合ってなかったら、メール送信
    # === 送受信先
    Send_obj = Send_Mail('jimnet.co.jp', '587', 'natsume@jimnet.co.jp',
                         'パスワード', 'natsume@jimnet.co.jp', 'tokotoko33ok@gmail.com')

    Send_obj.Send_Mail_To()


file11.close()
file22.close()

# ===================================================================================
# ================================= ソース比較 END =======================================
# ===================================================================================
