#import math
#from random import shuffle
#
#def func():
#	s = raw_input('-->')
#	t = []
#
#	if len(s) > 4:
#		t.append(s[0])
#		l = list(s[1:len(s)-1])
#		shuffle(l)
#		t.append("".join(l))
#		t.append(s[len(s)-1])
#		text = "".join(t)
#	else:
#		t.append(s)
#		text = "".join(t)
#	print text
#
#func()


# -*- coding: utf-8 -*-

import random, codecs, sys, random

def Typo(words):
    lis = words.split()
    for i in range(len(lis)):
        if len(lis[i]) <= 4:
            continue
        else:
            a = lis[i][0]
            b = lis[i][-1]
            x = [lis[i][1:len(lis[i] ) -1][j] for j in range(len(lis[1:len(lis[i]) -1]))]
            random.shuffle(x)
            y = "".join(x)
            lis[i] = "{}{}{}".format(a, y, b)
    lis = " ".join(lis)
    return lis

a = "Now I need a drink alcoholic of course after the heavy lectures involving quantum mechanics"
print Typo(a)
