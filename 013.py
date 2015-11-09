#013.py
# -*- coding: utf-8 -*-
#2015/11/09

import sys

def merge(input1, input2):
	with open(input1, "r") as f1, open(input2, "r") as f2:
		for line1, line2 in zip(f1, f2):
			print line1.rstrip("\n")+"\t"+line2,

if __name__ == "__main__":
	merge(sys.argv[1], sys.argv[2])

#python 013.py col1.txt col2.txt
#高知県	江川崎
#埼玉県	熊谷
#岐阜県	多治見
