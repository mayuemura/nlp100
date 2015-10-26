#038.py
# -*- coding: utf-8 -*-

import mod036
import matplotlib.pyplot as plt

data = list()

for pair in mod036.counter():
	data.append(pair[1])

plt.hist(data, bins=100, range=None, align="mid")
plt.ylim(0,100)
plt.xlabel("出現頻度")
plt.ylabel("単語の種類数")
plt.show()

"""
python 038.py < neko.txt.mecab
"""
