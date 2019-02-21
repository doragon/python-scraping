import requests
import sys
from bs4 import BeautifulSoup
from data.card_info import CardInfo
from util.file import File


path = 'assets/title.txt'
f = File(path)
titles, links = f.getTitleAndLinkList()

for i in range(len(titles)):
  print(str(i) + ' : ' + titles[i])
print('出力したい項目を選び、番号を入力してください。')
index = input()
title = ''
link = ''
try:
  title = titles[int(index)]
  link = links[int(index)]
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
    # print(ci.link)
    # ci.getDetail()
    # break

# CSV出力
f.write(csvList)
