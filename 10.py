f = open("hightemp.txt","r")
i = -1
for line in f:
    i += 1
i += 1
print i
f.close()
#24


f = open("hightemp.txt","r")
j = -1
for j,line in enumerate(f):
    pass
else:
    j += 1
print j
f.close()
#24


f = open("hightemp.txt","r")
l = f.readlines()
print len(l)
f.close()
#24
