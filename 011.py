#011.py
#-*- coding:utf-8 -*-
#2015/11/09

import sys

def tab_replace(input_file):
	with open(input_file, "r") as f:
		for line in f:
			print line.replace("\t", " "),

if __name__ == "__main__":
	tab_replace(sys.argv[1])

#python 011.py hightemp.txt
#高知県 江川崎 41 2013-08-12
#埼玉県 熊谷 40.9 2007-08-16
#岐阜県 多治見 40.9 2007-08-16
