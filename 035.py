#035.py
# -*- coding: utf-8 -*-

import sys
import mod030

np = list()
for sent in mod030.mapping():
	for i in range(len(sent)-1):
		dic = sent[i]
		dic_next = sent[i+1]

		if np == []:	#連接の最初の単語
			if dic["pos"] == "名詞" and dic_next["pos"] == "名詞":
				np.append(dic["surface"])
			else:
				pass

		else:			#2つめ以降
			if dic["pos"] == "名詞":
				np.append(dic["surface"])
			else:
				
				for word in np:
					print word,
				print "\n"
				np = list()

"""
python 035.py < neko.txt.mecab

人間 中 

一番 獰悪 

時 妙 

一 毛 

その後 猫

"""
