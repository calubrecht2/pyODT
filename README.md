pyODT
=====

A Python library to handle Open Document word processor files. 

First major feature is odt diff

odt diff
Compares two odt files on a paragraph by paragraph basis, displaying diffs.
Also examines the lists of images and reports any changes.


----

To use this diff with git:
add a .gitattributes file, telling git to use an alternate diff for odt files
 

*.odt diff=odt

Then set up the odt diff tool in your config

git config --global diff.odt <path>/extDiffODT

make sure pyODT is in your PYTHONPATH
