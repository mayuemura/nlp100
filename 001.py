#-*- coding:utf-8 -*-
#001.py
#2015/10/19

import sys

def main(input_str):
	input_u = unicode(input_str)

	print input_u[::2]

	print "".join([word for i, word in enumerate(input_u) if i % 2 == 0])

if __name__ == "__main__":
	main(sys.argv[1])

#python 001.py "パタトクカシーー"
