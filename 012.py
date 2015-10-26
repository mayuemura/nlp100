#
#
#def func():
#
#    f = codecs.open("hightemp.txt","r","utf-8")
#    i = 0
#    fo = []
#
#    for line in f.readlines():
#        for i in range(2):
#            fo.append(codecs.open("col%d.txt" % (i+1),"w","utf-8"))
#            fo[i].write(line[i])
#
#    f.close()
#    for i in range(2):
#        fo[i].close()
#
#func()




# -*- coding: utf-8 -*-

import sys, codecs

f = codecs.open("hightemp.txt", "r", "utf-8")
col1 = u""
col2 = u""
error = 0

for line in f:
    line.replace("\t", " ")
    temp = line.split()
    if len (temp) < 2:
        error = -1
        break
    else:
        col1 = col1 + temp[0] + "\n"
        col2 = col2 + temp[1] + "\n"

f.close()

if error == -1:
    print "Error happened"
else:
    fw1 = codecs.open("col1.txt", "w", "utf-8")
    fw2 = codecs.open("col2.txt", "w", "utf-8")

    fw1.write(col1)
    fw2.write(col2)

    fw1.close()
    fw2.close()

 

