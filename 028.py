#028.py
# -*- coding: utf-8 -*-

import re
import sys

d = dict()
pattern = re.compile(r"<ref.+|<br.+?>")
pattern2 = re.compile(r"\{\{lang\|.+?\|(.+?)\}\}")

for line in sys.stdin:
	item = list(line.split(" ",1))

	item[1] = pattern.sub("",item[1])
	item[1] = pattern2.sub(r"\1", item[1])

	d[item[0]] = item[1]

for k, v in d.iteritems():
	print k, v,

"""
python 025.py < england.txt | python 026.py | python 027.py | python 028.py

公式国名 United Kingdom of Great Britain and Northern Ireland
ccTLD .uk / .gb
GDP値元 1兆5478億

"""
