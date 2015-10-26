#mod036.py
# -*- coding: utf-8 -*-

import sys
import mod030
from collections import Counter

def counter():
    words = list()
    c = Counter()
    for sent in mod030.mapping():
        for dic in sent:
            words.append(dic["surface"])

    c = Counter(words)
    return c.most_common()

if __name__ == "__main__":
    for pair in counter():
        print pair[0],pair[1]
