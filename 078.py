#078.py
#estimate_accuracy
# -*- coding:utf-8 -*-

import sys

def estimate(result):
	count = 0.0
	accuracy = 0.0
	precision = 0.0
	recall = 0.0
	F1 = 0.0
	for line in result:
		if line.startswith("*****"):
			count += 1
		elif line.startswith("Accuracy"):
			accuracy += float(line.split()[1])
		elif line.startswith("Micro P"):
			item = line.split()
			precision += float(item[4])
			recall += float(item[6])
			F1 += float(item[8])
	e_accuracy = round(accuracy/count, 6)
	e_precision = round(precision/count, 6)
	e_recall = round(recall/count, 6)
	e_F1 = round(F1/count, 6)
	return e_accuracy, e_precision, e_recall, e_F1


if __name__ == "__main__":
	estimated = estimate(sys.stdin)
	print "Accuracy: {}".format(estimated[0])
	print "Precision: {}".format(estimated[1])
	print "Recall: {}".format(estimated[2])
	print "F1: {}".format(estimated[3])


"""
classias-train -tb -g5 -x feature.txt | python 078.py

Accuracy: 0.741811
Precision: 0.745003
Recall: 0.742311
F1: 0.742169
"""
