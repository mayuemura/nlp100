#039.py
# -*- coding: utf-8 -*-

import mod036
import matplotlib.pyplot as plt

data = list()
count = list()

for i, pair in enumerate(mod036.counter()):
	data.append(pair[1])
	count.append(i)

plt.loglog(count, data)
plt.xlabel("出現頻度順位")
plt.ylabel("出現頻度")
plt.show()
