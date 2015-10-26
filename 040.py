#040.py
# -*- coding: utf-8 -*-

import sys


class Morph(object):

	def __init__(self):
		self.surface = ""
		self.base = ""
		self.pos = ""
		self.pos1 = ""

	def process(self, line):
		word = line.split("\t")
		if len(word) < 2:
			pass
		else:
			self.surface = word[0]
			words = word[1].split(",")
			self.base = words[6]
			self.pos = words[0]
			self.pos1 = words[1]

			return self

	def show(self):
		print "s:%s, b:%s, p:%s, p1:%s" % (self.surface, self.base, self.pos, self.pos1)

if __name__ ==  "__main__":

	sentence = list()
	text = list()

	if int(sys.argv[1]) < 1:	#0を指定されたとき
		print "Error!"

	else:
		indx = int(sys.argv[1]) - 1

		for line in sys.stdin:
			if line.startswith("*"):
				pass
			else:
				m = Morph()
				result = m.process(line)
				if line.startswith("EOS"):
					if not sentence == []:
						text.append(sentence)
						sentence = list()
					else:		#空行処理
						sentence.append(m)
						text.append(sentence)
						sentence = list()
				else:
					sentence.append(result)

		for item in text[indx]:
				item.show()


"""
python 040.py 3 < neko.txt.cabocha


s:　, b:　, p:記号, p1:空白
s:どこ, b:どこ, p:名詞, p1:代名詞
s:で, b:で, p:助詞, p1:格助詞
s:生れ, b:生れる, p:動詞, p1:自立
s:た, b:た, p:助動詞, p1:*
s:か, b:か, p:助詞, p1:副助詞／並立助詞／終助詞
s:とんと, b:とんと, p:副詞, p1:一般
s:見当, b:見当, p:名詞, p1:サ変接続
s:が, b:が, p:助詞, p1:格助詞
s:つか, b:つく, p:動詞, p1:自立
s:ぬ, b:ぬ, p:助動詞, p1:*
s:。, b:。, p:記号, p1:句点

"""
