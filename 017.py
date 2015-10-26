# -*- coding: utf-8 -*-

import codecs

f = codecs.open("hightemp.txt", "r", "utf-8")
l1 = u""
for line in f:
    words = line.split()    #単語に分ける
    l1 = l1 + words[0] + "\n"     #1列目

t = u""
s = set(l1.split())
t = "\n".join(s)

print t 


f.close()
