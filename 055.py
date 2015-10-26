#055.py
# -*- coding:utf-8 -*-

import sys
from lxml import etree

def main():
	root = etree.parse(sys.stdin)
	tokens = root.xpath("/root/document/sentences/sentence/tokens/token")

	name = list()
	for token in tokens:
		if token.find("NER").text == "PERSON":
			name.append(token.find("word").text)
		elif not name == []:
			for i in name:
				print i,
			print ""
			name = []
		else:
			pass

if __name__ == "__main__":
	main()

"""
python 055.py < nlp.txt.xml

Alan Turing 
Joseph Weizenbaum 
MARGIE 
Schank 
Wilensky 
Meehan 
Lehnert 
Carbonell 
Lehnert 
Jabberwacky 
Moore 
"""

