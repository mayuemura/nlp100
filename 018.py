# -*-coding :utf-8 -*-

import codecs
f = codecs.open("hightemp.txt", "r", "utf-8")

i = 0
words = []
w = u""
for line in f:
    words.append(line.split())

print words[0]

s = sorted(words, key= lambda x:x[2])
for i in range(len(s)):
    w = w + "\t".join(s[i]) + "\n"
    i += 1

print w
