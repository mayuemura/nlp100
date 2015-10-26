#075.py
# -*- coding:utf-8 -*-

def main():
	feature = dict()
	with open("sentiment.model", "r") as f:
		for line in f:
			if line.startswith("@"):
				pass
			else:
				item = line.split()
				feature[item[1]] = float(item[0])
	A = sorted(feature.items(), key=lambda x:x[1], reverse=True)
	B = sorted(feature.items(), key=lambda x:x[1])
	versions = [A, B]

	for version in versions:
		i = 1
		for k, v in version:
			print k, v
			if i == 10:
				break
			i += 1
		print "------------"

if __name__ == "__main__":
	main()

"""
python 075.py

engrossing 1.5599
entertaining 1.42782
unexpected 1.4206
refreshing 1.2819
help 1.24675
provides 1.22263
rare 1.21669
cinema 1.19727
wonderful 1.15633
mesmerizing 1.09811
------------
dull -1.62788
fails -1.59449
boring -1.54456
worst -1.45189
bore -1.39346
intention -1.28102
waste -1.24039
mediocre -1.22793
lack -1.21107
unfunny -1.20178
------------
"""
