#083test.py
#-*- coding:utf-8 -*-

import sys
import json
from collections import Counter

@profile

def main(context_file):
	l = list()
	for line in context_file:
		context = json.loads(line)
		for k, v in context.iteritems():
			for word in v.split("\t"):
				l.append((k, word))
	print dict(Counter(l))

if __name__ == "__main__":
	main(sys.stdin)
