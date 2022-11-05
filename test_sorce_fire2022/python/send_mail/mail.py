from smtplib import SMTP

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from email.utils import formatdate

from email.mime.text import MIMEText  # MIME 形式データ用
from email.utils import formatdate
import smtplib


class Send_Mail():

    def __init__(self, host, port, account, password, from_email, to_email):
        self.host = host
        self.port = port
        self.account = account
        self.password = password
        self.from_email = from_email
        self.to_email = to_email

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
        subject = "テストメール3"
        message = "テストメール3"
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

        # ====== メール送信
        # server = smtplib.SMTP("SMTPサーバ", ポート番号)

        # デバッガ
        # server.set_debuglevel(True)
        # === 送受信先
Send_obj = Send_Mail('jimnet.co.jp', 'port', 'natsume@jimnet.co.jp',
                     'パスワード', 'natsume@jimnet.co.jp', 'tokotoko33ok@gmail.com')

Send_obj.Send_Mail_To()
