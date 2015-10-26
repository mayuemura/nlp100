#morph.py
# -*- coding: utf-8 -*-

import sys


class Morph(object):
    def __init__(self,surface,base,pos,pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

    def show(self):
        print "surface:%s, base:%s, pos:%s, pos1:%s" % (self.surface, self.base, self.pos, self.pos1)


def morphs():
    morphlist = list()
    for line in sys.stdin:
        if line.startswith("EOS"):
            if morphlist == []:
                pass
            else:
                yield morphlist
                morphlist = list()
        elif line.startswith("*"):
            pass
        else:
            word = line.split("\t")
            surface = word[0]
            words = word[1].split(",")
            base = words[6]
            pos = words[0]
            pos1 = words[1]
            m = Morph(surface, base, pos, pos1)
            morphlist.append(m)

if __name__ ==  "__main__":

    count = 0
    indx = int(sys.argv[1])
    for mlist in morphs():
        if count == indx:
            for instance in mlist:
                instance.show()
        count += 1


