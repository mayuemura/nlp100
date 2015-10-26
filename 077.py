#077.py
# -*- coding:utf-8 -*-

import sys

def main():
	all_count = 0.0			#全部
	accuracy_count = 0.0	#正解
	tp_fn = 0.0			#真T
	tp = 0.0			#予測T 真T
	tp_fp = 0.0			#予測T

	for line in sys.stdin:
		item = line.split("\t")
		answer = item[0]
		predict = item[1]

		all_count += 1.0

		if predict == "+1":
			tp_fp += 1.0
			if answer == "+1":
				tp += 1.0

		if answer == "+1":
			tp_fn += 1.0

		if answer == predict:
			accuracy_count += 1.0

	accuracy = round(accuracy_count/all_count, 4)
	precision = round(tp/tp_fp, 4)
	recall = round(tp/tp_fn, 4)
	f1 = round(2*precision*recall/(precision+recall), 4)

	print "Accuracy:", accuracy
	print "Precision:", precision
	print "Recall:", recall
	print "F1:", f1

if __name__ == "__main__":
	main()


"""
python 076.py < sentiment.txt | python 077.py

Accuracy: 0.9446
Precision: 0.9495
Recall: 0.939
F1: 0.9442
"""
