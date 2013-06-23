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
    return self._archive.open("content.xml").read()

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

  def diff(self, other):
    if isinstance(other, str):
      other = ODT(other)
    s1 = self.getContentAsText().splitlines()
    s2 = other.getContentAsText().splitlines()
    differ = difflib.context_diff(s1, s2, fromfile=self._filename, tofile=other._filename, lineterm='')
    diffS = ''
    for line in differ:
      diffS += line + '\n'
    return diffS
