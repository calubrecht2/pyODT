import zipfile
import xml.sax

class ODT:
  def __init__(self, fileName):
    self._archive = zipfile.ZipFile(fileName)
  
  def close(self):
    self._archive.close()

  def getContent(self):
    return self._archive.open("content.xml").read()

  class ODTContentHandler(xml.sax.ContentHandler):
    def __init__(self):
      self._buffer = ''
      self._inParagraph = False

    def startElement(self, name, attrs):
      if name == "text:p":
        if self._inParagraph:
          raise Exception("Nested paragraphs were not expected")
        self._inParagraph = True

    def characters(self, ch):
      if self._inParagraph:
        self._buffer += ch

    def endElement(self, name):
      if name == "text:p":
        self._inParagraph = False
        self._buffer += '\n'

  def getContentAsText(self):
    parser = xml.sax.make_parser()
    handler = self.ODTContentHandler()
    parser.setContentHandler(handler)
    parser.parse(self._archive.open("content.xml"))
    return handler._buffer 
     
