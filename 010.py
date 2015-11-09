#010.py
#-*- coding:utf-8 -*-
#2015/11/09

import sys
from collections import Counter

def linecount(input_file):
	with open(input_file) as f:
		print max(i for i, line in enumerate(f, start=1))
		#なんで通るのかわからない…

if __name__ == "__main__":
	linecount(sys.argv[1])

#python 010.py hightemp.txt
#24
