#060.py

# -*- coding: utf-8 -*-

import plyvel
import json
import sys

def main():
	db = plyvel.DB("/tmp/area.db", create_if_missing=True)
	for line in sys.stdin:
		js = json.loads(line)
		key = js.get(u"name", u"None").encode("utf-8")	#nameをkeyとする
		value = js.get(u"area", u"None").encode("utf-8")
		db.put(key, value)

	db.close()

if __name__ == "__main__":
	main()

"""
gzcat artist.json.gz | python 060.py
"""
