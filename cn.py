# -*- coding:utf-8 -*-

import re
import json

def main():

	ptrn = re.compile(r"\|\s\[\[([A-Za-z\s]+)\]\]\s.*")
	f = open("countries.txt", "r")
	fo = open("countryname.txt", "w")
	l = list()
	for line in f:
		m = ptrn.match(line)
		if m:
			l.append(m.group(1))
	fo.write(json.dumps(l))
	f.close()
	fo.close()

if __name__ == "__main__":
	main()
