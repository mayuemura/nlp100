#056.py
# -*- coding:utf-8 -*-

import sys
from lxml import etree

def coref(root):
	corefs = root.xpath("/root/document/coreference/coreference")
	for coref in corefs:
		mentions = coref.xpath("mention")
		re_word = ""
		for mention in mentions:
			if re_word == "":
				re_word = mention.findtext("text")
				
			else:
				sent_num = int(mention.findtext("sentence"))
				start_num = int(mention.findtext("start"))
				end_num = int(mention.findtext("end"))
				indx = [sent_num, start_num, end_num]
				yield re_word, indx		#tuple

def replace(root):
#	print coref_set.next()

	sentences = root.xpath("/root/document/sentences/sentence")
	for sentence in sentences:
		sentenceid = int(sentence.get("id"))

		for now_coref in coref(root):

			if sentenceid == now_coref[1][0]:
				tokens = sentence.xpath("tokens/token")

				for token in tokens:
					tokenid = int(token.get("id"))

					if tokenid == now_coref[1][1]:
						print token.findtext("word")
						token.find("word").set("word",now_coref[0])
						print token.findtext("word")+""

					else:
						pass

			else:
				pass


if __name__ == "__main__":
	root = etree.parse(sys.stdin)
	replace(root)

#	for item in replace(root):
#		print item

#	for item in coref(root):
#		print item
