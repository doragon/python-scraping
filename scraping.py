import requests
from bs4 import BeautifulSoup


class CardInfo:
  def __init__(self, no, cardType, element, name, rare, link):
    self.no = no
    self.cardType = cardType
    self.element = element
    self.name = name
    self.rare = rare
    self.link = link
  
  def print(self):
    separator = ','
    tmp = self.no \
      + separator \
      + self.element \
      + separator \
      + self.name \
      + separator \
      + self.rare
    tmp = tmp.replace('\n', '').replace(' ', '')
    print(tmp)


# ここに調べたいリンクを設定
url = '/wiki/%E3%83%9D%E3%82%B1%E3%83%A2%E3%83%B3%E3%82%AB%E3%83%BC%E3%83%89%E3%82%B2%E3%83%BC%E3%83%A0_%E3%82%B5%E3%83%B3%26%E3%83%A0%E3%83%BC%E3%83%B3_%E3%83%8F%E3%82%A4%E3%82%AF%E3%83%A9%E3%82%B9%E3%83%91%E3%83%83%E3%82%AF_GX%E3%82%A6%E3%83%AB%E3%83%88%E3%83%A9%E3%82%B7%E3%83%A3%E3%82%A4%E3%83%8B%E3%83%BC'
target_url = 'https://wiki.xn--rckteqa2e.com' + url

# requestsを使って、webから取得
r = requests.get(target_url)
# 要素を抽出
soup = BeautifulSoup(r.text, 'lxml')

table = soup.find_all('table', {'class' : 'bluetable'})[0]
rows = table.findAll('tr')

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
    ci.print()
