#014.py
# -*- coding: utf-8 -*-
#2015/11/09

import sys

def head(input_file, n):
	with open(input_file, "r") as f:
		for i in range(n):
			print f.readline(),


if __name__ == "__main__":
	head(sys.argv[1], int(sys.argv[2]))

#python 014.py hightemp.txt 4
#高知県	江川崎	41	2013-08-12
#埼玉県	熊谷	40.9	2007-08-16
#岐阜県	多治見	40.9	2007-08-16
#山形県	山形	40.8	1933-07-25

