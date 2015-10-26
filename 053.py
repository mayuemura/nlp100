#053.py
# -*- coding:utf-8 -*-

import sys
from lxml import etree

def main():
	root = etree.parse(sys.stdin)
	token = root.xpath("/root/document/sentences/sentence/tokens/token/word")
	for word in token:
		print word.text

if __name__ == "__main__":
	main()

"""
python 053.py < nlp.txt.xml

Natural
language
processing
From
Wikipedia
,
the
free
"""
