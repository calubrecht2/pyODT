import zipfile

class ODT:
  def __init__(self, fileName):
    self._archive = zipfile.ZipFile(fileName)
    self._contentXML = self._archive.open("content.xml").read()
  
  def close(self):
    self._archive.close()

  def getContent(self):
    return self._contentXML
