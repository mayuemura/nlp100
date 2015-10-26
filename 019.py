# -*- coding: utf-8 -*-

import codecs

f = codecs.open("hightemp.txt", "r", "utf-8")
l1 = u""
i = 0
for line in f:
    words = line.split()
    l1 = l1 + words[0] + "\n"
    i += 1           #行数カウント

s = set(l1.split())  #文字列の集合(重複なし)
count = [0]*len(s)   #集合の文字列の出現回数
w = list(s)          #集合をリストに変換


a = 0
b = 0
lines = []

while b < len(s):    #集合の要素に対して1つずつ確認
    while a < i:
        if l1.split()[a] == w[b]:
            count[b] = count[b] + 1
        a += 1
    lines.append([w[b], str(count[b])])
    b += 1
    a = 0

print lines[0]

text = u""
j = 0
s = sorted(lines, key=lambda x:x[1])
for j in range(len(s)):
    text = text + "\t".join(s[j]) + "\n"
    j += 1

print text


