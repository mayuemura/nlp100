#-+- coding: utf-8 -*-
#000.py
#2015/10/19

import sys

def main(input_str):

	l = list(input_str)
	l.reverse()
	print "".join(l)

	print input_str[::1]
	#最初から最後まで1つずつ
	print input_str[::-1]
	#最初から最後まで後ろから1つずつ

if __name__ == "__main__":
	main(sys.argv[1])

#python 000.py "stressed"
