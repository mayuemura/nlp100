#083.py
#-*- coding:utf-8 -*-

import sys
import json
from collections import defaultdict, Counter

def main(infile, outfile):

	tc = defaultdict(Counter)
	for line in infile:
		t, c = line.rstrip("\n").split("\t")
		tc[t][c] += 1

	#N = len(c)

	for k in tc.iterkeys():
		for v, i in tc[k].iteritems():
			outfile.write("{}\t{}\t{}\n".format(k, v, i))

if __name__ == "__main__":
	main(sys.stdin, sys.stdout)
