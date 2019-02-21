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
  
  def format(self, tmp):
    # 改行、半角スペース、全角スペースの削除
    return tmp.replace('\n', '').replace(' ', '').replace('　', '')

  def getCsv(self):
    separator = ','
    tmp = self.no \
      + separator \
      + self.cardType \
      + separator \
      + self.element \
      + separator \
      + self.name \
      + separator \
      + self.rare
    return self.format(tmp)
  
  def getDetail(self):
    target_url = 'https://wiki.xn--rckteqa2e.com' + self.link
    r = requests.get(target_url)
    soup = BeautifulSoup(r.text, 'lxml')
    table = soup.find_all('table', {'class' : 'blueinfobox'})[0]

    store = {}
    preKey = ''
    rows = table.findAll('tr')
    for row in rows:
      th = row.th
      td = row.td

      if th != None and td != None:
        key = self.format(th.get_text())
        value = self.format(td.get_text())
        store[key] = [value]
        preKey = key
      elif th != None:
        key = self.format(th.get_text())
        if key.find('No') != -1:
          store['no'] = [key]
        else:
          store['name'] = [key]
      elif td != None:
        value = self.format(td.get_text())
        store[preKey].append(value)
    return store
