import requests
import sys
from bs4 import BeautifulSoup
from data.card_info import CardInfo
from util.file import File


# title.txtの読み込み
path = 'assets/title.txt'
f = File(path)
titles = f.getTitleList()

# title一覧を表示し、ユーザー入力を求める
for i in range(len(titles)):
  items = titles[i].split(',')
  if len(items) != 4:
    continue
  # 略称が設定されているかチェック
  if items[0] == '' or items[0] == None:
    continue
  # リンクが設定されているかチェック
  if items[3] == '' or items[3] == None:
    continue
  # 略称:名称(発売日)
  print(str(i) + ' : ' + items[0] + ':' + items[1] + '(' + items[2] + ')')
print('出力したい項目を選び、番号を入力してください。')
index = input()

# 選択されたリンクを取得
link = ''
try:
  items = titles[int(index)].split(',')
  link = items[3]
except:
  print('意図しない入力データのため、実行が終了しました。')
  sys.exit()

# 参照先のURLを作成
target_url = 'https://wiki.xn--rckteqa2e.com' + link
# requestsを使って、webから取得
r = requests.get(target_url)
# 要素を抽出
soup = BeautifulSoup(r.text, 'lxml')

table = soup.find_all('table', {'class' : 'bluetable'})[0]
rows = table.findAll('tr')

csvList = []
storeList = []
for row in rows:
  info = row.findAll('td')
  if len(info) != 0:
    ci = CardInfo(
      info[0].get_text()
      , info[1].get_text()
      , info[2].get_text()
      , info[3].get_text()
      , info[4].get_text()
      , info[3].a.get('href')
    )
    csv = ci.getCsv()
    csvList.append(csv)
    try:
      store = ci.getDetail()
      storeList.append(str(store))
      print(csv)
    except:
      print(csv + ' の取得に失敗しました。')

# ファイル名の設定
items = titles[int(index)].split(',')
filename_csv = 'output/csv/' + items[0] + '_' + items[1] + '_csv.txt'
filename_detail = 'output/detail/' + items[0] + '_' + items[1] + '_detail.txt'

# CSV出力
f.writeTextFile(filename_csv, csvList)
print('CSV出力が完了しました。')

# カード詳細情報出力
f.writeTextFile(filename_detail, storeList)
print('カード詳細情報出力が完了しました。')
