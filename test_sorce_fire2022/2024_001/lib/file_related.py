import os


class File_related ():

    @staticmethod
    def File_Write(path_w, get_text):
        """
        指定されたパスにテキストデータを書き込む 静的メソッド。
        :param path_w: 書き込み先のファイルパス
        :param get_text: 書き込むテキストデータ
        """
        try:
            with open(path_w, mode='wb') as f:
                for item in get_text:
                    print("item:::アイテム:::" + item)
                    f.write(item.encode('utf-8'))
            print(f"ファイル {path_w} に書き込みました。")
        except IOError as e:
            print(f"ファイル {path_w} の書き込み中にエラーが発生しました: {e}")

    @staticmethod
    def File_Append(path_w, get_text):
        """
        指定されたパスにテキストデータを追記する 静的メソッド。
        :param path_w: 書き込み先のファイルパス
        :param get_text: 書き込むテキストデータ
        """
        try:
            with open(path_w, mode='ab') as f:
                for item in get_text:
                    print("item:::アイテム:::" + item)
                    f.write(item.encode('utf-8'))
            print(f"ファイル {path_w} に追記しました。")
        except IOError as e:
            print(f"ファイル {path_w} の追記中にエラーが発生しました: {e}")

    @staticmethod
    def Check_Dir(dir_path):
        """
        パスにディレクトリが存在していない場合はディレクトリ作成。
        :param path: ディレクトリのパス
        """
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
            print(f"ディレクトリ {dir_path} を作成しました。")
        else:
            print(f"ディレクトリ {dir_path} は既に存在します。")
