#020.py
# -*- coding: utf-8 -*-
import json
import sys

for line in sys.stdin:
    d = json.loads(line.strip())
    if d["title"] == u"イギリス":
        sys.stdout.write(d["text"])

"""
gzcat jawiki-country.json.gz | python 020.py > england.txt
"""

"""
#標準出力じゃないやつ
import codecs
import gzip

f = gzip.open("jawiki-country.json.gz", "rb")
fw = codecs.open("england.txt", "w", "utf-8")

for line in f:
    d = json.loads(line.strip())
    if d["title"] == u"イギリス":
        print d["text"]
        fw.write(d["text"])

f.close()
fw.close()
"""
