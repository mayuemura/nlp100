def Ngram(n):
	s = raw_input('-->')
	k = 0

	word = s.split()
	for k in range(len(word)-n+1):
		print word[k:k+n]

	print "-----------"

	text  = "".join(word)
	st = list(text)
	for k in range(len(str)-n+1):
		print st[k:k+n]

Ngram(2)
	

