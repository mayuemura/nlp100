#012.py
# -*- coding: utf-8 -*-
#2015/11/09

import sys

def cut(input_text):
	with open("col1.txt", "w") as f1, open("col2.txt", "w") as f2:
		for line in input_text:
			a, b = line.split()[0:2]
			f1.write(a+"\n"), f2.write(b+"\n")

if __name__ == "__main__":
	cut(sys.stdin)

#python 011.py hightemp.txt | python 012.py
