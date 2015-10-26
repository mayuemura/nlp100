#068.py
# -*- coding:utf-8 -*-

from pymongo import MongoClient, ASCENDING, DESCENDING

def main():
	client = MongoClient()
	db = client.artistDB
	collection = db.artist
	for data in collection.find({"tags.value":"dance"}).sort("rating.value",DESCENDING).limit(10):
		print data.get("name"),
		print data.get("rating").get("value")


	client.close()

if __name__ == "__main__":
	main()

"""
python 068.py
SHäuptling 100
Boy George 100
Toni Basil 100
Milk Inc. 100
digitalTRAFFIC 100
...

mongo
> col.find({"tags.value":"dance"},{"name":true,"rating.value":true).sort({"rating.value":-1}).limit(10)
{ "_id" : ..., "rating" : { "value" : 100 }, "name" : "SSHäuptling" }
{ "_id" : ..., "rating" : { "value" : 100 }, "name" : "Boy George" }
{ "_id" : ..., "rating" : { "value" : 100 }, "name" : "Toni Basil" }
{ "_id" : ..., "rating" : { "value" : 100 }, "name" : "Milk Inc." }
{ "_id" : ..., "rating" : { "value" : 100 }, "name" : "digitalTRAFFIC" }
"""
