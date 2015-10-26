# -*- coding: utf-8 -*-

import codecs

f1 = codecs.open("col1.txt", "r", "utf-8")
f2 = codecs.open("col2.txt", "r", "utf-8")
f3 = codecs.open("merge.txt", "w", "utf-8")

l1 = u""
l2 = u""

for line in f1:
    l1 = l1 + line

for line in f2:
    l2 = l2 + line

list1 = l1.split()
list2 = l2.split()


#list1 = []
#list2 = []
#for line in f1:
#    list1.append(line)
#for line in f2:
#    list2.append(line)

i = 0
t = u""
for i in range(len(list1)):
    t = t + (list1[i] + "\t" + list2[i]+ "\n")

f3.write(t)

f1.close()
f2.close()
f3.close()

