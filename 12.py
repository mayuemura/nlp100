# -*- coding: utf-8 -*-
import codecs

def func():

    f = codecs.open("hightemp.txt","r","utf-8")
    i = 0
    fo = []

    for line in f.readlines():
        for i in range(2):
            fo.append(codecs.open("col%d.txt" % (i+1),"w","utf-8"))
            fo[i].write(line[i])

    f.close()
    for i in range(2):
        fo[i].close()


func()


#col1.txt:高埼岐山山和静山埼群群愛千静愛山岐群千埼大山山愛
#col2.txt:知玉阜形梨歌岡梨玉馬馬知葉岡媛形阜馬葉玉阪梨形知 
