pyODT
=====

A Python library to handle Open Document word processor files. First goal is a textual diff.


odt diff
First, open zipfile and read in content.xml, parsing xml.
Build up unformatted text block, reading text:p tags as paragraphs.
Diff the text.

Diff the files in Pictures?

Go through content.xml again and diff changes in styling?
