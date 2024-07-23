class Config_Setting():
    # ディレクトリ設定
    LOG_DIR = "/Python_ソース比較_2022/test_sorce_fire2022/2024_001/LOG/"

    # 原本（格納ディレクトリ）
    ORIGINAL_DIR = "/Python_ソース比較_2022/test_sorce_fire2022/2024_001/ORIGINAL_DIR/"
    # 比較用（格納ディレクトリ）
    COMPARISON = "/Python_ソース比較_2022/test_sorce_fire2022/2024_001/COMPARISON/"

    # 対象 URL
    READ_URL = "https://192.168.254.204/kdemo/index.php"

    # ソース名
    SOURCE_01 = "index.html"
    SOURCE_02 = "login.html"
    SOURCE_03 = "reserve_list.html"
    SOURCE_04 = "view_list.html"

    @staticmethod
    def get_config():
        """
        設定を辞書形式で取得する
        """
        return {
            "LOG_DIR": Config_Setting.LOG_DIR,
            "READ_URL": Config_Setting.READ_URL
        }
