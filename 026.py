#026.py
# -*- coding: utf-8 -*-

import re
import sys

d = dict()
pattern = re.compile(r"''+")

for line in sys.stdin:
	item = list(line.split(" ", 1))
	for m in pattern.finditer(item[1]):
		item[1] = pattern.sub("", item[1])

	d[item[0]] = item[1]

for k, v in d.iteritems():
	print k, v,

"""
gzcat jawiki-country.json.gz | python 025.py | python 026.py

公式国名 {{lang|en|United Kingdom of Great Britain and Northern Ireland}}<ref>英語以外での正式国名:<br/>
ccTLD [[.uk]] / [[.gb]]<ref>使用は.ukに比べ圧倒的少数。</ref>
首都 [[ロンドン]]
GDP値 2兆3162億<ref name="imf-statistics-gdp" />
確立形態4 現在の国号「グレートブリテン及び北アイルランド連合王国」に変更
GDP統計年 2012
"""
