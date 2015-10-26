#079.py
# -*- coding:utf-8 -*-

import sys
import matplotlib.pyplot as plt
import mod076

def main(text):
	r = list()

	for result in mod076.main(text):
		item = result.split("\t")
		answer = item[0]
		prob = float(item[2])
		r.append((answer, prob))

	for i in range(10):
		threshold = i/10.0
		l = list()

		for item in r:
			answer = item[0]
			prob = item[1]
			predict = "-1"

			if prob >= threshold:
				predict = "+1"
			l.append((answer, predict))

		tp = 0.0		#予測T 真T
		tp_fp = 0.0		#予測T
		tp_fn = 0.0		#真T

		for item in l:
			answer = item[0]
			predict = item[1]
			if predict == "+1":
				tp_fp += 1.0
				if answer == "+1":
					tp += 1.0

			if answer == "+1":
				tp_fn += 1.0

		if tp_fp == 0:
			precision = 1.0
		else:
			precision = round(tp/tp_fp, 4)
			recall = round(tp/tp_fn, 4)
		yield precision, recall

if __name__ == "__main__":
	x = list()
	y = list()
	for pair in main(sys.stdin):
		print pair
		x.append(pair[0])
		y.append(pair[1])
	plt.plot(x, y)
	plt.xlabel("再現率(recall)")
	plt.ylabel("適合率(precision)")
	plt.xlim(0.5, 1.1)
	plt.ylim(0.0, 1.1)
	plt.show()

"""
python 079.py < sentiment.txt
"""
