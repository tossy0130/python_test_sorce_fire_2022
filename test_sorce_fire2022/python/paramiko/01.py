import paramiko

import subprocess  # python 標準モジュール

# ssh 接続

with paramiko.SSHClient() as client:

    HOSTNAME = '127.0.0.1'  # ホスト
    USERNAME = ''  # ユーザ名
    PASSWORD = ''  # パスワード

#    KEY_FILENAME = ''

    LINUX_COMMAND = 'ls'

    # ssh 接続
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    client.connect(hostname=HOSTNAME, port=2222,
                   username=USERNAME, password=PASSWORD)

    stdin, stdout, stderr = client.exec_command(LINUX_COMMAND)

    for line in stdout:
        print(line, end='')

    proc = subprocess.run(["ls", "-l", "/etc/ssh"], capture_output=True)
    print(proc.stdout)
