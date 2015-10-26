#034.py
# -*- coding: utf-8 -*-

import sys
import mod030

for sent in mod030.mapping():
	for i in range(len(sent)-1):
		dic_no = sent[i]

		if dic_no["pos1"] == "連体化":
			dic_a = sent[i-1]
			dic_b = sent[i+1]
			print dic_a["surface"] + dic_no["surface"] + dic_b["surface"]

"""
python 034.py < neko.txt.mecab

彼の掌
掌の上
書生の顔
はずの顔
顔の真中
穴の中
"""

