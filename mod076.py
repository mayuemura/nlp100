#076.py
# -*- coding:utf-8 -*-

import sys
import mod074

def main(text):
	for line in text:
		item = line.split(" ",1)
		answer = item[0]
		result = mod074.polarity(item[1])

		yield "{}\t{pol}\t{prob}".format(answer,**result)

if __name__ == "__main__":
	for ans in main(sys.stdin):
		print ans
"""
python 076.py < sentiment.txt

-1	-1	0.110266
-1	-1	0.472627
+1	+1	0.786116
"""
