#027.py
#-*- coding: utf-8 -*-

import re
import sys

d = dict()
pattern = re.compile(r"\[\[(.+?)\]\]")

for line in sys.stdin:
	item = list(line.split(" ", 1))
	item[1] = pattern.sub(r"\1", item[1])
		#item[1] = pattern.sub(m.group(1), item[1])
		#だと、一行に2つ以上[[]]があるときにおかしくなる

	d[item[0]] = item[1]

for k, v in d.iteritems():
	print k, v,



"""
python 025.py < england.txt | python 026.py | python 027.py

GDP統計年元 2012
ISO 3166-1 GB / GBR
国章画像 ファイル:Royal Coat of Arms of the United Kingdom.svg|85px|イギリスの国章
標語 {{lang|fr|Dieu et mon droit}}<br/>（フランス語:神と私の権利）
国際電話番号 44
確立形態3 グレートブリテン及びアイルランド連合王国建国<br />（連合法 (1800年)|1800年連合法）


-m.group(1)のときの結果-
確立形態3 グレートブリテン及びアイルランド連合王国建国<br />（グレートブリテン及びアイルランド連合王国）
""" 

