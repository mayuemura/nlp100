#066.py
# -*- coding:utf-8 -*-

from pymongo import MongoClient

def main():
	client = MongoClient()
	db = client.artistDB
	collection = db.artist
	print collection.find({"area":"Japan"}).count()
	client.close()

if __name__ == "__main__":
	main()

"""
python 066.py
29614

mongo
>use artistDB
>col = db.artist
>col.find({"area":"Japan"}).count()
29614
"""
