import os
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

import win32com.client
import pythoncom

app = Flask(__name__)
UPLOAD_FOLDER = 'upload_folder/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


# === index
@app.route('/')
def root_page():
    return render_template('index.html')


# === ファイルアップロード画面
@app.route('/upload')
def upload():

    # アップロード ディレクトリ
    f_path = r'D:\Python_ソース比較_2022\test_sorce_fire2022\python\PDF\upload_folder'

    # Excelファイル　出力先
    outputDir = f_path + r'\out_put'

    # === ディレクトリ作成
    if os.path.exists(outputDir):
        return render_template('upload.html')
    else:
        os.makedirs(outputDir)
        return render_template('upload.html')

# === ファイルアップロード　処理


@app.route('/upload_file', methods=['POST'])
def upload_file():

    # アップロード ディレクトリ
    f_path = r'D:\Python_ソース比較_2022\test_sorce_fire2022\python\PDF\upload_folder'

    # Excelファイル　出力先
    outputDir = f_path + r'\out_put'

    # 操作したいソフト 指定
    pythoncom.CoInitialize()
    excel = win32com.client.Dispatch("Excel.Application")

    # ====== POST 送信　があった場合
    if request.method == 'POST':

        # === ファイルアップロード　処理
        files = request.files.getlist('file')
        for file in files:
            file.save(os.path.join(
                app.config['UPLOAD_FOLDER'], secure_filename(file.filename)))
        #    return 'file uploaded successfully'

        # ====== ファイル存在チェック　
        for file in os.listdir(f_path):
            # === 「Excel」ファイルがあった場合

            if file.endswith('.xlsx'):

                # f_path から　ファイルを取得して　ループ処理
                for f in os.listdir(f_path):
                    # ファイル名 と　拡張子　に分ける

                    base, ext = os.path.splitext(f)

                    if ext == '.xlsx' and '~$' not in base:
                        # パス と　ファイル名　を結合
                        wb = excel.Workbooks.Open(os.path.join(f_path, f))

                        wb.WorkSheets(1).Select()
                        # PDF へ　変換 ExportAsFixedFormat(0)
                        wb.ActiveSheet.ExportAsFixedFormat(
                            0, outputDir + '\\' + base + '.pdf')
                        wb.Close()

                return (f_path + '\\' + file)

            # === 「word」ファイルがあった場合
            elif file.endswith('.doc') or file.endswith('.docx'):
                return (f_path + '\\' + file)


if __name__ == '__main__':
    app.run()
