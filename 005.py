#005.py
# -*- coding: utf-8 -*-
#2015/10/26
import sys


def ngram(input_list, n):
	k = 0
	for k in range(len(input_list)-n+1):
		print input_list[k:k+n]

if __name__ == "__main__":
	ngram(sys.argv[1], int(sys.argv[2]))
	ngram(sys.argv[1].split(), int(sys.argv[2]))
	
#python 005.py "I am an NLPer" 2
#I
# a
#am
#...
#'I', 'am']
#['am', 'an']
#['an', 'NLPer']

