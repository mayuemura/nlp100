#081.py
#-*- coding: utf-8 -*-

import sys
import re
import json

ptrn = re.compile(r".*?\s.*")
def main(infile, outfile):

	with open("countryname.txt", "r") as f:
		country = list()
		l = json.loads(f.read())

	for name in l:
		m = ptrn.match(name)
		if m:
			country.append(name)
	country.reverse()

	for line in infile:
		for name in country:
			line = re.sub(name, name.replace(" ", "_"), line)
		outfile.write(line)

if __name__ == "__main__":
	main(sys.stdin, sys.stdout)


#...clocks using the phase of VLF radio signals The United_States Naval Observatory began
