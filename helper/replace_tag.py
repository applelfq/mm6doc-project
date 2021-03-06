#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib_mate import Path
from dataIO.textfile import read, write, readlines

tags = list(readlines("tag.txt"))

path = r"D:\Workspace\py34\py34_projects\mm6doc-project\source\09-旅行时间表\content.rst"
text = read(path)

for tag in tags:
    text = text.replace(tag, " :ref:`%s` " % tag)

write(text, path)
