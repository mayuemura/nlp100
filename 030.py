#030.py
# -*- coding: utf-8 -*-

import sys


def mapping():
	text = list()
	sentence = list()
	for line in sys.stdin:
		d = dict()
		if line.startswith("EOS"):
			if sentence == []:
				pass
			else:
				text.append(sentence)
				sentence = list()
			pass
		else:
			node = line.split("\t")
			d["surface"] = node[0]

			mor = node[1].split(",")
			d["base"] = mor[6]	#-3だと基本形じゃないやつがあるので6
			d["pos"] = mor[0]
			d["pos1"] = mor[1]

			sentence.append(d)
	return text


if __name__ == "__main__":

	for i in mapping():
		for j in i:
			print "{",
			for k, v in j.iteritems():
				print "{}:{}".format(k, v),
			print "}"
		print "\n"

"""
cat neko.txt.mecab | python 030.py


{base:一 pos:名詞 surface:一 pos1:数 }


{ base:　 pos:記号 surface:　 pos1:空白 }
{ base:吾輩 pos:名詞 surface:吾輩 pos1:代名詞 }
{ base:は pos:助詞 surface:は pos1:係助詞 }
{ base:猫 pos:名詞 surface:猫 pos1:一般 }
{ base:だ pos:助動詞 surface:で pos1:* }
{ base:ある pos:助動詞 surface:ある pos1:* }
{ base:。 pos:記号 surface:。 pos1:句点 }

"""
