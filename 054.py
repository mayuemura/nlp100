#054.py
# -*- coding:utf-8 -*-

import sys
from lxml import etree

def main():
	root = etree.parse(sys.stdin)
	tokens = root.xpath("/root/document/sentences/sentence/tokens/token")

	for token in tokens:
		word = token.find("word").text
		lemma = token.find("lemma").text
		pos = token.find("POS").text

		print "{}\t{}\t{}".format(word, lemma, pos)

if __name__ == "__main__":
	main()

"""
python 054.py < nlp.txt.xml

Natural	natural	JJ
language	language	NN
processing	processing	NN
From	from	IN
Wikipedia	Wikipedia	NNP
,	,	,
the	the	DT

"""
