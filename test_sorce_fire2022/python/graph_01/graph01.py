import matplotlib as mpl
import matplotlib.pyplot as plt
# pyplotモジュールを"plt"という名前でインポートする


# ================================ 折れ線グラフ
x = [0, 1, 2, 3]  # x座標
y = [1, 5, 2, 6]  # y座標


plt.plot(x, y, color="k")  # 点列(x,y)を黒線で繋いだプロット
plt.show()  # プロットを表示

# ================================ END 折れ線グラフ
