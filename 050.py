#050.py
# -*- coding: utf-8 -*-

import sys
import re

def main():
	pattern = re.compile(r"(.+?[.;:?!])\s(?=[A-Z])")	#(?=...)...が続くときだけmatch
	for line in sys.stdin:
		if pattern.finditer(line):
			for m in pattern.finditer(line):
				print m.group(1)

		else:
			print line		#文になってないやつとり出せない

if __name__ == "__main__":
	main()

"""
python 050.py < nlp.txt

Natural language processing (NLP) is a field of computer science, artificial intelligence, and linguistics concerned with the interactions between computers and human (natural) languages.

As such, NLP is related to the area of humani-computer interaction.

The history of NLP generally starts in the 1950s, although work can be found from earlier periods.

The Georgetown experiment in 1954 involved fully automatic translation of more than sixty Russian sentences into English.
"""
