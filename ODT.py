import zipfile
import xml.sax
import difflib

class ODT:
  def __init__(self, fileName):
    self._archive = zipfile.ZipFile(fileName)
    self._filename = fileName
  
  def close(self):
    self._archive.close()

  def getContent(self):
    return self.getFile("content.xml")

  def listImages(self):
    return filter(lambda x : x.startswith("Pictures/"), self.listFiles())

  def getFile(self, fileName):
    return self._archive.open(fileName).read()

  def listFiles(self):
    return map(lambda x: x.filename, self._archive.filelist)

  class ODTContentHandler(xml.sax.ContentHandler):
    """
      Reads content.xml from the odt and extracts all the text inside text:p
      tags"""
    def __init__(self):
      self._buffer = ''
      self._paragraphCount = 0

    def startElement(self, name, attrs):
      if name == "text:p":
        self._paragraphCount += 1

    def characters(self, ch):
      if self._paragraphCount > 0:
        self._buffer += ch

    def endElement(self, name):
      if name == "text:p":
        self._paragraphCount -= 1
        self._buffer += '\n'

  def getContentAsText(self):
    parser = xml.sax.make_parser()
    handler = self.ODTContentHandler()
    parser.setContentHandler(handler)
    parser.parse(self._archive.open("content.xml"))
    return handler._buffer 

  def diffText(self, other):
    if isinstance(other, str):
      other = ODT(other)
    s1 = self.getContentAsText().splitlines()
    s2 = other.getContentAsText().splitlines()
    differ = difflib.context_diff(s1, s2, fromfile=self._filename, tofile=other._filename, lineterm='', n=1)
    diffS = ''
    for line in differ:
      diffS += line + '\n'
    return diffS
  
  def diff(self, other):
    return self.diffText(other) + '------\n' + self.diffImages(other)

  def diffImages(self, other):
    if isinstance(other, str):
      other = ODT(other)
    selfimgs = self.listImages()
    otherimgs = other.listImages()
    modifiedimgs = []
    selfimgs.sort()
    otherimgs.sort()
    newimgs = list(set(otherimgs) - set(selfimgs))
    delimgs = list(set(selfimgs) - set(otherimgs))
    for img in (set(selfimgs) - set(delimgs)):
      selfI = self.getFile(img)
      otherI = self.getFile(img)
      if selfI != otherI:
        modifiedimgs.append(img)

    diffS =  '%s new images: %s\n' % (str(len(newimgs)), str(newimgs))
    diffS += '%s deleted images: %s\n' % (str(len(delimgs)), str(delimgs))
    diffS += '%s modified images: %s' % (str(len(modifiedimgs)), str(modifiedimgs))
    return diffS
      
  
  def diff_charwise(self, other):
    '''
    Diffs two files, shows differences on a character by character basis.
    Need to come up with a better output format.'''

    if isinstance(other, str):
      other = ODT(other)
    s1 = self.getContentAsText()
    s2 = other.getContentAsText()
    differ = difflib.context_diff(s1, s2, fromfile=self._filename, tofile=other._filename, lineterm='')
    diffS = ''
    for line in differ:
      diffS += line + '\n'
    return diffS
