#024.py
# -*- coding: utf-8 -*-
import re
import sys

pattern = re.compile(r"\[*(ファイル|File):(.+?)\|")
for line in sys.stdin:
    for s in pattern.finditer(line):
        print s.group(2)

"""
gzcat jawiki-country.json.gz | python 020.py | python 024.py
Royal Coat of Arms of the United Kingdom.svg
Battle of Waterloo 1815.PNG
The British Empire.png
Uk topo en.jpg
BenNevis2005.jpg
"""
