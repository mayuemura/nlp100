#041.py
# -*- coding: utf-8 -*-

import sys
from mod040 import Morph #040.py

class Chunk(Morph):

	def __init__(self):
		Morph.__init__(self)
		self.morphs = list()
		self.dst = None #?
		self.srcs = list()

	def chunk(self, line):

		next_src = list()


		if line.startswith("EOS"):
			pass

		elif line.startswith("*"):
			element = line.split()

			if not self.morphs == []:
				return self

			if element[2] == "-1D":
				if not self.src == []:
					self.src = next_src
					next_src = list()

			else:
				self.dst = int(element[2].rstrip("D"))	#係り先index
				next_src.append(int(element[1]))		#係り元indexのリスト

		else:
			self.morphs = Moprh.process(line)


	def show(self):
		print "morphs:[ s:%s, b:%s, p:%s, p1:%s ]" % (self.surface, self.base, self.pos, self.pos1)
		print "dst: %s, src: %s" #%sでいいんだっけ？

if __name__ == "__main__":

