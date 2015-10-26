#065.py
# -*- coding:utf-8 -*-

from pymongo import MongoClient

def main():
	client = MongoClient()
	db = client.artistDB
	collection = db.artist
	for data in collection.find({"name":"Queen"}):
		print data
	client.close()

if __name__ == "__main__":
	main()

"""
python 065.py

{u'name': u'Queen', u'area': u'Japan', u'gender': u'Female', u'tags': [{u'count': 1, u'value': u'kamen rider w'}, {u'count': 1, u'value': u'related-akb48'}], u'sort_name': u'Queen', u'ended': True, u'gid': u'420ca290-76c5-41af-999e-564d7c71f1a7', u'_id': ObjectId('559f37833fadcc03ae6277c4'), u'type': u'Character', u'id': 701492, u'aliases': [{u'name': u'Queen', u'sort_name': u'Queen'}]}
...

mongo
>use artistDB
>col = db.artist
>col.find({"name":"Queen"})

{ "_id" : ObjectId("559f37833fadcc03ae6277c4"), "name" : "Queen", "tags" : [ { "count" : 1, "value" : "kamen rider w" }, { "count" : 1, "value" : "related-akb48" } ], "gender" : "Female", "area" : "Japan", "sort_name" : "Queen", "ended" : true, "gid" : "420ca290-76c5-41af-999e-564d7c71f1a7", "type" : "Character", "id" : 701492, "aliases" : [ { "name" : "Queen", "sort_name" : "Queen" } ] }
...

"""
