#033.py
# -*- coding: utf-8 -*-

import sys
import mod030

for i in mod030.mapping():
	for j in i:
		if j["pos1"] == "サ変接続":
			print j["surface"]
#	print "\n-------------------"

"""
mecab neko.txt > neko.txt.mecab | python 033.py

見当
記憶
話
装飾
突起
運転
記憶
"""
