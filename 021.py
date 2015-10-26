#021.py
# -*- coding: utf-8 -*-
import re
import sys 

 
words = re.compile(r"\[\[Category:")
for line in sys.stdin:
    if words.match(line):
        print line,
 
"""
gzcat jawiki-country.json.gz | python 020.py | python 021.py
[[Category:イギリス|*]]
[[Category:英連邦王国|*]]
[[Category:G8加盟国]]
[[Category:欧州連合加盟国]]
[[Category:海洋国家]]
[[Category:君主国]]
[[Category:島国|くれいとふりてん]]
[[Category:1801年に設立された州・地域]]
"""
