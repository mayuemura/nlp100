#023.py
# -*- coding: utf-8 -*-
import re
import sys

"""
for line in sys.stdin:
    if re.match("==", line):
        c = line.count("=")
        level = c/2-1
        section = line.rstrip().replace("=", "")
        print "{}  level {}".format(section, level)
"""


pattern = re.compile(r"(=+)(.+?)(=+)")
for line in sys.stdin:
    m = pattern.match(line)

    if m:
        level = len(m.group(1))-1
        section = m.group(2) 
        print "{}  level:{}".format(section, level)


"""
gzcat jawiki-country.json.gz | python 020.py | python 023.py
国名  level 1
歴史  level 1
地理  level 1
気候  level 2
政治  level 1
外交と軍事  level 1
"""
