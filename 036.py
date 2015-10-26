#036.py
# -*- coding: utf-8 -*-

import sys
import mod030
from collections import Counter

def counter():
	words = list()

	for sent in mod030.mapping():
		for dic in sent:
			words.append(dic["base"])

	c = Counter(words)
	return c.most_common()

if __name__ == "__main__":
	for pair in counter():
		print pair[0],pair[1]


"""
python 036.py < neko.txt.mecab

の 9194
。 7486
て 6868
、 6772
は 6420
に 6243
を 6071
と 5508
が 5337
た 3988
"""

