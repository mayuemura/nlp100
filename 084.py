#084.py
#-*- coding:utf-8 -*-

import sys
import math
from collections import defaultdict, Counter

def main(infile, outfile):

	tc = defaultdict(dict)
	N = 0.0

	for line in infile:
		t, c , f = line.rstrip("\n").split("\t")
		tc[t][c] = f
		N += 1.0

	high_freq = list()
	for t in tc.iterkeys():
		for c, f in tc[t].iteritems():
			if int(f) >= 5:	#10
				high_freq.append((t, c, f))


	for t, c, f in high_freq:

		ft = 0
		for freq in tc[t].values():
			ft += float(freq)

		fc = 0
		for value in tc.values():
			if c in value.keys():
				fc += float(value[c])

		value = max(math.log(N*float(f)/(ft*fc)), 0)

		outfile.write("{}\t{}\t{}\n".format(t, c, value))


if __name__ == "__main__":
	main(sys.stdin, sys.stdout)

#'limited': {'not': '1'}, 
#'all': {'anarchists': '1', 'anarchism': '1', 'of': '2', 'forms': '1', 'oppose': '1', 'Many': '1', 'not': '1'}

#bzcat context.txt.bz2 | python 083.py | python 084.py
#of		the		0.264732375033
#from	the		0.487875926348
#in		the		0.862569375789
#the	of		0
#the	from	0.581760182625
#the	the		0
