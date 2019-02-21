class File:
  def __init__(self, path):
    self.path = path

  def getTitleAndLinkList(self):
    titles = []
    links = []
    f = open(self.path, 'r', encoding='utf-8')
    while True:
      title, link = f.readline(), f.readline()
      if not title:
        break
      titles.append(title.replace('\n', ''))
      links.append(link.replace('\n', ''))
    f.close
    return titles, links

  def write(self, csvList):
    text = "\n".join(csvList)
    with open('list.txt', 'w', encoding='utf-8') as f:
      f.write(text)
