def Ngram(s,n):
	k = 0
	a = []

	word = s.split()
	text = "".join(word)
	str = list(text)

	for k in range(len(str)-n+1):
		ngram = "".join(str[k:k+n])
		a.append(ngram)
	return a

X = set(Ngram("paraparaparadise",2))
Y = set(Ngram("paragraph",2))

U = X | Y
I = X & Y
C = X ^ Y

print U
print I
print C

if 'se' in X:
	print "'se' is in X"
else:
	print "'se' is not in X"

if 'se' in Y:
	print "'se' is in Y"
else:
	print "'se' is not in Y"


