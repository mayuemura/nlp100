#064.py
# -*- coding:utf-8 -*-
from pymongo import MongoClient, ASCENDING, DESCENDING
import sys
import json
import time

def main():
	client = MongoClient()
	db = client.artistDB
	collection = db.artist

	js = list()
	for line in sys.stdin:
		js.append(json.loads(line))

	collection.insert(js)
	client.close()

if __name__ == "__main__":
#	main()
	t1 = time.time()

	client = MongoClient()
	db = client.artistDB
	collection = db.artist

	collection.create_index([("name",ASCENDING)])
	collection.create_index([("aliases.name", ASCENDING)])
	collection.create_index([("tags.value", ASCENDING)])
	collection.create_index([("rating.value", DESCENDING)])

	for data in collection.find({u"name":u"Al Street"}):
		print data.get("area", "None")

	print time.time() - t1, "sec"
	client.close()

"""
gzcat artist.json.gz | python 064.py

United States
United States
...
United States
Netherlands
0.00680303573608 sec

"""
