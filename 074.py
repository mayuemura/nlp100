#074.py
# -*- coding:utf-8 -*-

import sys
import math
from nltk.stem.wordnet import WordNetLemmatizer

lmtzr = WordNetLemmatizer()
stopwords = list()
with open("stopword.txt", "r") as f:
	for word in f:
		stopwords.append(word.strip())

	
def input_feature(text):
	ifeature = ""
	for word in text.split():
		if word in stopwords:
			pass
		else:
			ifeature += " " + lmtzr.lemmatize(word)
	return ifeature


def feature():
	feature = dict()
	with open("sentiment.model", "r") as f:
		for line in f:
			if line.startswith("@"):
				pass
			else:
				item = line.split()
				feature[item[1]] = float(item[0])
	return feature
feature = feature()


def polarity(text):
	score = 0
	words = input_feature(text).split()
	for word in words:
		score += feature.get(word, 0.0)
	score += feature.get("__BIAS__")

	if score > 0:
		pol = "+1"
	else:
		pol = "-1"

	d = {"pol":pol, "prob":round(prob(score), 6)}
	return d


def prob(score):
	A = math.exp(-1*score)
	P = 1/(1+A)
	return P


if __name__ == "__main__":
	print "polarity:{pol} probability:{prob}".format(**polarity(sys.argv[1]))

"""
python 074.py "this movie is the best"
polarity:+1 probability:0.665694

python 074.py "this movie is the worst"
polarity:-1 probability:0.166532
"""

