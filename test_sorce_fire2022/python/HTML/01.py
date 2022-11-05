from bs4 import BeautifulSoup, BeautifulStoneSoup
import requests
from urllib.parse import urlparse


# soup = BeautifulSoup(open('python/HTML/diff.html',
#                     encoding='utf-8'), 'html.parser')

#response = requests.get(get_url, verify=False)
#html_text = BeautifulSoup(response.text, 'lxml')

#

# HTML ファイル 日本語に置換

with open('python/HTML/diff.html', encoding='utf-8') as f:
    data_lines = f.read()

data_lines = data_lines.replace('Added', '追加')
data_lines = data_lines.replace('Changed', '変更')
data_lines = data_lines.replace('Deleted', '削除')

data_lines = data_lines.replace('(f)irst change', '最初の変更')
data_lines = data_lines.replace('(n)ext change', '次の変更')
data_lines = data_lines.replace('(t)op', '上')

with open('python/HTML/diff.html', mode='w', encoding='utf-8') as f:
    f.write(data_lines)
