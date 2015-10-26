# -*- coding: utf-8 -*-
import codecs

def tail(n):
    f = codecs.open("hightemp.txt","r","utf-8")
    lines = []

    for line in f:
        lines.append(line)

    i = len(lines)-n

    while i < len(lines):
        print lines[i]
        i += 1
    f.close() 

n = input("-->")
tail(n)


#-->3
#山梨県	大月	39.9	1990-07-19
#山形県	鶴岡	39.9	1978-08-03
#愛知県	名古屋	39.9	1942-08-02
