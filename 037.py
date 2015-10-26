#037.py
# -*- coding: utf-8 -*-

import sys
import mod036
import matplotlib.pyplot as plt

name = list()
Y = list()

wordnum = int(sys.argv[1])
X = range(wordnum)

for pair in mod036.counter():
	name.append(pair[0])
	Y.append(pair[1])
	if len(name) == wordnum:
		break


plt.bar(X, Y, align = "center")
plt.xticks(X, name)
plt.xlabel("単語")
plt.ylabel("出現回数")
plt.title("単語の出現頻度")
plt.show()

"""
python 037.py 10 < neko.txt.mecab
"""
