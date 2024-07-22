from bs4 import BeautifulSoup, BeautifulStoneSoup


# ======================= テスト ===========================
soup = BeautifulSoup(html_content, 'html.parser')

# <th> タグを全て取得
th_tags = soup.find_all('th')

# <th> タグ内の文字列を出力
for th_val in th_tags:
    print("val:::" + th_val + "\n")
