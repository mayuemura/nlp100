#052.py
# -*- coding:utf-8 -*-

import sys
import re
from stemming.porter2 import stem

def main():
	for line in sys.stdin:
		word = line.rstrip()
		print word+"\t"+ stem(word)

if __name__ == "__main__":
	main()

"""
python 050.py < nlp.txt | python 051.py | python 052.py

Natural	Natur
language	languag
processing	process
(NLP)	(NLP)
is	is
a	a
field	field
"""
