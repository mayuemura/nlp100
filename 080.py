#080.py
# -*- coding: utf-8 -*-

import sys

def main(infile, outfile):

	for line in infile:
		token_list = list()
		for token in line.split():
			p_token = token.strip(".,!?;:()[]'\"")
			if not p_token == "":
				token_list.append(p_token)
		outfile.write(" ".join(token_list)+"\n")

if __name__ == "__main__":
	main(sys.stdin, sys.stdout)

#bzcat hoge.txt.bz2 | python 080.py | bzip2 -z > corpus.txt.bz

