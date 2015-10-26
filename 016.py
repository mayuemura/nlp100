# -*- coding: utf-8 -*-

import codecs

def split(n):

    f = codecs.open("hightemp.txt", "r", "utf-8")
    fo = []

    i = 0
    lines =[]
    for line in f:  #行数カウント
        i += 1
        lines.append(line)

    m = i/n         #1分割あたりの行数

    for k in range(n):
        fo.append(codecs.open("split%d.txt" % (k+1), "w", "utf-8"))

    k = 0
    j = 0
    count = j + m
    while k <n:            #n分割
        while j < count:   #1分割あたり
            fo[k].write(lines[j])
            j += 1
        k += 1
        count = j + m


    for k in range(n):
        fo[k].close()
        print "split%d.txt " % (k+1)


n = input("-->")
split(n)
