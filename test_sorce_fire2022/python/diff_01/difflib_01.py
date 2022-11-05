import os
import difflib

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

for data_02 in output_diff02:

    if data_02[0:1] in ['+', '-']:
        print(data_02)

file11.close()
file22.close()
