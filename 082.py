#082.py
#-*- coding: utf-8 -*-

import sys
import random

def main(infile, outfile):

	for line in infile:
		text = line.split()

		for i, token in enumerate(text):
			width = random.randint(1,5)

			for indx in range(max(0, i-width), min(i+width, len(text))):
				if  i != indx:
					outfile.write("{}\t{}\n".format(token, text[indx]))


if __name__ == "__main__":
	main(sys.stdin, sys.stdout)
