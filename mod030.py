#mod030.py
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
            d["base"] = mor[-3]
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

