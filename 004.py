#-*- coding:utf-8 -*-
#004.py
#2015/10/19

input_str = "Hi He Lied Because Could Not Oxidize Fluorine. " + \
			"New Nations Might Alse Sign Peace Security Clause. Arthur King Can."

def main():
	indx_set = (1,5,6,7,8,9,15,16,19)
	d = dict()

	for i, word in enumerate(input_str.split()):
		if i+1 in indx_set:
			d[word[0]] = i+1
		else:
			d[word[0:2]] = i+1
	print d

if __name__ == "__main__":
	main()
