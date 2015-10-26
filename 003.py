#-*- coding:utf-8 -*-
#003.py
#2015/10/19

input_str = "Now I need a drink, alcoholic of cource, " + \
			"after the heavy lectures involving quantum machanics."

def main():
	
	word_list = list()
	for word in input_str.split():
		word_list.append(word.rstrip(".,"))

	print "".join([str(len(word)) for word in word_list])

if __name__ == "__main__":
	main()
