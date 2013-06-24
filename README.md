pyODT
=====

A Python library to handle Open Document word processor files. First goal is a textual diff.


odt diff
First, open zipfile and read in content.xml, parsing xml.
Build up unformatted text block, reading text:p tags as paragraphs.
Diff the text.

Diff the files in Pictures?

Go through content.xml again and diff changes in styling?


----

To use this diff with git:
add a .gitattributes file, telling git to use an alternate diff for odt files
 

*.odt diff=odt

Then set up the odt diff tool in your config

git config --global diff.odt <path>/extDiffODT

make sure pyODT is in your PYTHONPATH
