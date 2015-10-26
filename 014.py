# -*- coding: utf-8 -*-
import codecs


def head(n):
    f = codecs.open("hightemp.txt","r","utf-8")
    i = 0

    for i in range(n):
        print f.readline()
    f.close()


n = input('-->')
head(n)

#-->3
#高知県	江川崎	41	2013-08-12
#埼玉県	熊谷	40.9	2007-08-16
#岐阜県	多治見	40.9	2007-08-16
