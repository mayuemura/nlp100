#067.py
# -*- coding:utf-8 -*-

from pymongo import MongoClient

def main():
	client = MongoClient()
	db = client.artistDB
	collection = db.artist
	for data in collection.find({"aliases.name":"!Disdain"}):
		print data.get("name")

	client.close()

if __name__ == "__main__":
	main()


"""
python 067.py
Distain!
Distain!

mongo
>use artistDB
>col = db.artist
>col.find({"aliases.name":"!Disdain"},{"name":true})
{ "_id" : ObjectId("559f30f33fadcc02d93506ad"), "name" : "Distain!" }
{ "_id" : ObjectId("559f37733fadcc03ae5c657d"), "name" : "Distain!" }
"""
