import re
import requests
import sys
from bs4 import BeautifulSoup
from data.card_info import CardInfo
from util.file import File


def getTitleList():
  path = 'assets/title.txt'
  f = File(path)
  return f.getTitleList()

def isTargetPack():
  print('拡張パックまたはその他(スターターなど)を選び、番号を入力してください。')
  print('0 : 拡張パック')
  print('1 : その他(スターターなど)')
  index = input()
  if index == '0':
    return True
  elif index == '1':
    return False
  else:
    print('意図しない入力データのため、実行が終了しました。')
    sys.exit()

def getNameAndLinkList():
  nameList = []
  linkList = []
  targetIndex = 0
  for t in titles:
    items = t.split(',')
    if len(items) != 4:
      continue
    # 略称が設定されているかチェック
    if items[0] == '' or items[0] == None:
      continue
    # リンクが設定されているかチェック
    if items[3] == '' or items[3] == None:
      continue
    # 略称:名称(発売日)
    tmp = str(targetIndex) + ' : ' + items[0] + ':' + items[1] + '(' + items[2] + ')'
    # 略称に数値が含まれているものが拡張パック
    result = re.match('.*\d.*', items[0])
    if isPack and result:
      targetIndex = targetIndex + 1
      nameList.append(tmp)
      linkList.append(items[3])
    elif not isPack and not result:
      targetIndex = targetIndex + 1
      nameList.append(tmp)
      linkList.append(items[3])
  return nameList, linkList

def selectTarget(targetList):
  for t in targetList:
    print(t)
  print('出力したい項目を選び、番号を入力してください。')
  return input()

def getTargetLink(linkList, index):
  try:
    return linkList[int(index)]
  except:
    print('意図しない入力データのため、実行が終了しました。')
    sys.exit()

def getCsvAndDetailList(target_url):
  # requestsを使って、webから取得
  r = requests.get(target_url)
  # 要素を抽出
  soup = BeautifulSoup(r.text, 'lxml')
  table = soup.find_all('table', {'class' : 'bluetable'})[0]
  rows = table.findAll('tr')

  csvList = []
  detailList = []
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
        detail = ci.getDetail()
        detailList.append(str(detail))
        print(csv)
      except:
        print(csv + ' の取得に失敗しました。')
  return csvList, detailList

def output(names, csvList, detailList):
  path_csv = 'output/csv/' + names[0] + '_' + names[1] + '_csv.txt'
  path_detail = 'output/detail/' + names[0] + '_' + names[1] + '_detail.txt'
  # CSV出力
  f = File(path_csv)
  f.writeTextFile(csvList)
  print('CSV出力が完了しました。')
  # カード詳細情報出力
  f = File(path_detail)
  f.writeTextFile(detailList)
  print('カード詳細情報出力が完了しました。')


if __name__ == '__main__':
  # title.txtの読み込み
  titles = getTitleList()

  # 拡張パックorその他(スターターなど)を表示し、ユーザー入力を求める
  isPack = isTargetPack()

  # 拡張パックorその他(スターターなど)でリストを作成する
  nameList, linkList = getNameAndLinkList()

  # title一覧を表示し、ユーザー入力を求める
  index = selectTarget(nameList)
  # 選択されたリンクを取得
  link = getTargetLink(linkList, index)

  # 参照先のURLを作成
  target_url = 'https://wiki.xn--rckteqa2e.com' + link
  # 参照先のカード一覧データおよび、カードごとの詳細データを取得
  csvList, detailList = getCsvAndDetailList(target_url)

  # ファイル名の設定
  names = nameList[int(index)].split(' : ')
  names = names[1].split(':')
  output(names, csvList, detailList)
