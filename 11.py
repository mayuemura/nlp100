fi = open("hightemp.txt")
fo = open("hightemp2.txt", "w")

for l in fi:
    fo.write(l.replace("	"," "))

fi.close()
fo.close()
