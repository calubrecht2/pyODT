import zipfile

def findFile(archive, fileName):
  for fileInfo in archive.filelist:
    if fileInfo.filename == fileName:
      return fileInfo
  return None

class ODT:
  def __init__(self, fileName):
    self._archive = zipfile.ZipFile(fileName)
    self._contentXML = self._archive.open(findFile(self._archive, "content.xml")).readlines()
  
  def close(self):
    self._archive.close()


  def getContent(self):
    return self._contentXML
