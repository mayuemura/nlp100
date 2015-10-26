#-*- coding:utf-8 -*-
#002.py
#2015/10/19

import sys

def main(input1, input2):
	l1 = list(unicode(input1))
	l2 = list(unicode(input2))
	print "".join([x+y for (x, y) in zip(l1, l2)])


if __name__ == "__main__":
	main(sys.argv[1], sys.argv[2])
#python 002.py "パトカー" "タクシー"
