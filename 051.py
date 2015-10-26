#051.py
# -*- coding: utf-8 -*-

import sys
import re

def main():
	for line in sys.stdin:
		word_list = line.split()
		for word in word_list:
			re.sub(r"[.;:?!]","",word)
			print word
		print ""

if __name__ == "__main__":
	main()

"""
python 050.py < nlp-small.txt | python 051.py

computers
and
human
(natural)
languages.

As
such,
NLP
"""
