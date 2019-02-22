class File:
  def __init__(self, path):
    self.path = path

  def getTitleList(self):
    titles = []
    f = open(self.path, 'r', encoding='utf-8')
    while True:
      title = f.readline()
      if not title:
        break
      titles.append(title.replace('\n', ''))
    f.close
    return titles

  def writeTextFile(self, filename, list):
    text = "\n".join(list)
    with open(filename, 'w', encoding='utf-8') as f:
      f.write(text)
