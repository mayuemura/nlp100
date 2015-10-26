# -*- coding: utf-8 -*-
import codecs


def head(n):
    f = codecs.open("hightemp.txt","r","utf-8")
    count = 0
    l = []
    i = 0

    while count < n:
        l.append(f.readline())
        count += 1

    while i < n:
        print l[i]
        i += 1

n = input('-->')
head(n)

#-->3
#高知県	江川崎	41	2013-08-12
#埼玉県	熊谷	40.9	2007-08-16
#岐阜県	多治見	40.9	2007-08-16
