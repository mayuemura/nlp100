#!/usr/bin/python
# -*- coding:utf-8 -*-
#069.py

import cgi
from jinja2 import Environment, FileSystemLoader
from pymongo import MongoClient

def main():

	requests = cgi.FieldStorage()

	name = requests.getvalue("name", None)
	aliases = requests.getvalue("aliases", None)

	query = dict()
	query["name"] = name
	query["aliases.name"] = aliases

	for k in query.keys():
		if query[k] == None:
			del query[k]

	if query == {}:	#全部findしてしまうのを回避
		query["name"] = None

	client = MongoClient()
	db = client.artistDB
	collection = db.artist.find(query)

	collection_list = list()
	for document in collection:
		collection_list.append(document)

	data = dict()

	data["name"] = name
	data["aliases"] = aliases
	data["collection"] = collection_list

	env = Environment(loader=FileSystemLoader("./", encoding="utf-8"))
	tmpl = env.get_template("069temp.html")
	print tmpl.render(data=data).encode("utf-8")

if __name__ == "__main__":
	main()
