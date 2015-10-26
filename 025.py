#025.py
# -*- coding: utf-8 -*-
import re
import sys

d = dict()
pattern = re.compile(r"\|(.+?) = (.+)")
for line in sys.stdin:
    if line.startswith("{{基礎情報"):
        for inner_line in sys.stdin:
            for m in pattern.finditer(inner_line):
                d[m.group(1)] = m.group(2)
            if inner_line.startswith("}}"):
                break
        break

for k, v in d.iteritems():
    print k, v

"""
gzcat jawiki-country.json.gz | python 020.py | python 025.py
GDP統計年元 2012
ISO 3166-1 GB / GBR
通貨 [[スターリング・ポンド|UKポンド]] (&pound;)
国際電話番号 44
公用語 [[英語]]（事実上）
~
動くけど↓のエラー(?)が出る
close failed in file object destructor:
sys.excepthook is missing
lost sys.stderr
"""
