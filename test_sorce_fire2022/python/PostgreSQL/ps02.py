import csv
import pprint

# === .csv カンマで区切る
with open(r'D:\\Python_ソース比較_2022\\test_sorce_fire2022\\python\\csv\\test_01.csv') as f:

    for val in f:
        tmp_arr = val.split(',')
        print(tmp_arr[0] + ' ' + tmp_arr[1] + ' ' + tmp_arr[2])
