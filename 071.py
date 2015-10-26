#071.py
# -*- coding:utf-8 -*-

import sys
import nltk
from collections import Counter

def frequency(words):
	stop_list_f = list()
	c = Counter(words)

	for pair in c.most_common():
		freq = pair[1]*1.0/len(words)*100
		if freq > 0.3:
			stop_list_f.append(pair[0])

	return stop_list_f

def pos(words):
	stop_list_p = set()
	pos_set = {":", "PRP", "IN", "DT", "CC", "CD"}

	for postags in nltk.pos_tag(words):
		if postags[1] in pos_set:
			stop_list_p.add(postags[0])

	return stop_list_p


def main():
	words = list()
	pos_set = set()

	for line in sys.stdin:
		one_line = line.lstrip("+-1 ").split()
		words.extend(one_line)	#nltkの操作を1回にしたい
	
	pos_set |= pos(words)
	freq_set = set(frequency(words))
	stop_word = pos_set | freq_set

	with open("stopword.txt", "w") as fw:
		fw.write("\n".join(stop_word))

####################################

stopwords = list()
with open("stopword.txt", "r") as f:
	for word in f:
		stopwords.append(word.strip())

def is_stopword(test_word):

	"""
	>>> print is_stopword("I")
	True
	>>> print is_stopword("an")
	True
	>>> print is_stopword("he")
	True
	>>> print is_stopword("effective")
	False
	"""
	test_word = test_word.lower()
	if test_word in stopwords:
		return True
	else:
		return False


if __name__ == "__main__":
#	main()
	import doctest
	doctest.testmod()



#nkf -w --overwrite sentiment.txt <--Unicodeに変換

