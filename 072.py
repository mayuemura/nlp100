#072.py
# -*- coding:utf-8 -*-

import sys
import nltk
from nltk.stem.wordnet import WordNetLemmatizer
from collections import Counter

lmtzr = WordNetLemmatizer()

def lemma(text):

	stopwords = list()
	with open("stopword.txt", "r") as f:
		for word in f:
			stopwords.append(word.strip())

	pos_list = ["RB", "JJ"]

	elem = text.split()
	pol = elem[0]
	sent = elem[1:]
	feature = pol

	for word in sent:
		if word in stopwords:
			pass
		else:
			if nltk.pos_tag([word])[0][1] in pos_list:
				feature += " " + lmtzr.lemmatize(word) + ":2.0"
			else:
				feature += " " + lmtzr.lemmatize(word) + ":1.0"
	feature += "\n" 
	return feature

if __name__ == "__main__":
	fw = open("feature.txt", "w")
	for line in sys.stdin:
		fw.write(lemma(line))
	fw.close()

"""
python 072.py < sentiment.txt
"""
