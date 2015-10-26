#063.py
# -*- coding:utf-8 -*-

import plyvel
import sys
import json
import pickle


def main():
	db = plyvel.DB("/tmp/tags.db", create_if_missing=True)

	for line in sys.stdin:
		js = json.loads(line)
		key = js.get(u"name", u"None").encode("utf-8")
		value = js.get(u"tags", u"None")
		values = pickle.dumps(value)
		db.put(key, values)

	db.close()

if __name__ == "__main__":
#	main()

	db = plyvel.DB("/tmp/tags.db", create_if_missing=True)
	query = sys.argv[1]
	value = db.get(query)
	values = pickle.loads(value)

	if not values == "None":
		for item in values:
			print "{}:{}".format(item["value"], item["count"])
	else:
		print "no tags"


"""
gzcat artist.json.gz | python 063.py "Love .45"
no tags

gzcat artist.json.gz | python 063.py "Lady Gaga"
gata rahe mera dil:1
the fame:1
united states:1
américain:1
...
"""
