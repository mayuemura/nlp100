#032.py
# -*- coding: utf-8 -*-

import sys
import mod030

for i in mod030.mapping():
	for j in i:
		if j["pos"] == "動詞":
			print j["base"],
	print "\n-------------------"

"""
mecab neko.txt > neko.txt.mecab | python 032.py

-------------------

-------------------

-------------------
生れる つく 
-------------------
する 泣く する いる 
-------------------
始める 見る 

"""
