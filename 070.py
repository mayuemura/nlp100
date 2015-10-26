#070.py
# -*- coding:utf-8 -*-

import sys
import random

def main():
	flag = 0
	f = open("sentiment.txt", "w")
	pol = list()

	for files in sys.argv[1:]:
		data = open(files, "r")

		if files.endswith("neg"):
			for line in data:
				pol.append("-1 "+line)

		elif files.endswith("pos"):
			for line in data:
				pol.append("+1 "+line)
		data.close()

	random.shuffle(pol)
	f.writelines(pol)

	f.close()

if __name__ == "__main__":
	main()

"""
python 070.py rt-polarity.neg rt-polarity.pos

-1 such a wildly uneven hit-and-miss enterprise... 
+1 the sweetest thing , a romantic comedy with ...
+1 morton is , as usual , brilliant .
"""
