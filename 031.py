#031.py
# -*- coding: utf-8 -*-

import sys
import mod030

for i in mod030.mapping():
	for j in i:
		if j["pos"] == "動詞":
			print j["surface"],
	print "\n-------------------"

"""
i, j ->普通数字に使う

cat neko.txt.mecab | python 031.py

-------------------

-------------------

-------------------
生れ つか 
-------------------
し 泣い し いる 
-------------------
始め 見 


"""
