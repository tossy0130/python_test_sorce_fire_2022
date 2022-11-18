from google.colab import drive
import os
import pandas as pd
from pandas import DataFrame
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline

drive.mount('/content/drive')

# === コラボラトリーまでのパス
os.chdir('/content/drive/My Drive/Colab Notebooks')

# === .csv 読み込み
# df = pd.read_csv('CSVファイル名', header = None)
df = pd.read_csv('ks-projects-201801.csv')

# df

# === ５行分　だけ　出力
# df.head()

# === データ数や平均、標準偏差、最小値、中央値、最高値
# df.describe()

"""
＊＊＊＊＊＊ df.describe() ＊＊＊＊＊＊ 
count：データ数
mean：平均値
std：標準偏差
min：最小値
25%：データを小さい順に並べ、25%の位置にある値(第1四分位数と呼ばれます)
50%：データを小さい順に並べ、50%の位置にある値(中央値と呼ばれます)
75%：データを小さい順に並べ、75%の位置にある値(第3四分位数と呼ばれます)
max：その列の最大値

"""
# データの行と列のサイズを見たい場合
# df.shape

"""
＊＊＊ 出力メモ ＊＊＊

dfが376881行×15列のデータ 

"""

"""
・新データの変数名 = 旧データの変数名.drop(['不要なカラム名1', '不要なカラム名2', '不要なカラム名3', ・・・], axis=1)

行名を指定して行を削除したい場合は、オプションとしてaxis=0

カラム名を指定して列を削除したい場合は、オプションとしてaxis=1

"""
# ========== カラム削除
# drop に指定した、引数のカラムを削除
df = df.drop(['ID', 'goal', 'pledged', 'pledged'], axis=1)

# df.head()

# ========== カラム名変更
# 新データの変数名 = 旧データの変数名.rename(columns = {'変更前カラム名1': '変更後カラム名1', '変更前カラム名2': '変更後カラム名2', ・・・})

df = df.rename(columns={'name': 'PJ名', 'category': '第2カテゴリー', 'main_category': '第1カテゴリー', 'currency': '通貨', 'deadline': '締切日',
               'launched': '開始日', 'state': '成否', 'backers': '支援者数', 'country': '国', 'usd_pledged_real': '支援額', 'usd_goal_real': '目標額'})

# df.head()

# ========= データの確認
# df.info()

# df['PJ名']
df['PJ名'].isnull()

# 欠損データだけを表示
df[df['PJ名'].isnull()]

# 欠損データに値を代入  no_name を入れる
df['PJ名'] = df['PJ名'].fillna('no_name')

# 指定した index の　行を確認
# df.loc[[166851, 307234, 309991, 338931]]

# df.info()

df['第2カテゴリー']

# 重複を取り除いて、カテゴリー数を表示
len(set(df['第2カテゴリー']))

# !　をつけることで、Linuxコマンドと認識させる。 （Googleコラボラトリー　での話）
!pip install japanize-matplotlib

fig = sns.countplot('第1カテゴリー', data=df)
fig.set_xticklabels(fig.get_xticklabels(), rotation=40, ha='right')

sns.countplot('通貨', data=df)

# === 通貨カラムが USD である行のみのデータセットを df に再代入
df = df[df['通貨'] == 'USD']
sns.countplot('通貨', data=df)

# === USD 通貨カラム　削除
df = df.drop('通貨', axis=1)
df.head()
