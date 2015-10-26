#022.py
# -*- coding: utf-8 -*-
import re
import sys

pattern = re.compile(r"\[\[Category:(.+?)\]\]")
for line in sys.stdin:
    m = pattern.match(line)
    if m:
        sys.stdout.write(m.group(1)+"\n")

"""
gzcat jawiki-country.json.gz | python 020.py | python 022.py
イギリス|*
英連邦王国|*
G8加盟国
欧州連合加盟国
海洋国家
君主国
島国|くれいとふりてん
1801年に設立された州・地域
"""


"""
f = open("england.txt", "r")
def multiple_replace(text, rx):
    def one_xlat(match):
        return adict[match.group(0)]
    return rx.sub(one_xlat, text)

adict = {
    "[[Category:"    : "",
    "]]"    : "",
}

rx = re.compile('|'.join(map(re.escape, adict)))

words = re.compile(r"\[\[Category:")
for line in f:
    if words.match(line):
        l = multiple_replace(line, rx)
        print l
"""
