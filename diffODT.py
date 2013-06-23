#!/usr/bin/env python

if __name__ == "__main__":
  from pyODT import ODT
  import sys
  file1 = sys.argv[1]
  file2 = sys.argv[2]
  odt1 = ODT(file1)
  odt2 = ODT(file2)
  print odt1.diff(odt2)


