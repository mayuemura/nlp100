#009.py
# -*- coding: utf-8 -*-
#2015/11/2

import random

def Typo(input_str):

    words = input_str.split()

    for word in words:

        if len(word) <= 4:
            yield word

        else:
			word_list = list(word)
			mix = list(word_list[1:-1])
			random.shuffle(mix)
			word_list[1:-1] = mix
			yield "".join(word_list)


if __name__ == "__main__":
	input_str = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
	print " ".join(word for word in Typo(input_str))

#python 009.py
#I cdolun't bveleie that I cloud allacuty untsneardd what I was rdaenig : the pneamhenol pwoer of the hmuan mind .
