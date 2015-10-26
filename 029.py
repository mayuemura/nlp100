#029.py
# -*- coding: utf-8 -*-

import re
import sys
import urllib


for line in sys.stdin:		#国旗画像のファイル名を得る
	if line.startswith("国旗画像"):
		item = list(line.split(" ", 1))
		title = item[1]

url = "http://ja.wikipedia.org/w/api.php?"	#api
params = urllib.urlencode(
		{'action': 'query',
		 'format': 'json',
		 'titles': "File:" + title,
		 'prop': 'imageinfo',
		 'iiprop': 'url',})
data = urllib.urlopen(url + params).read()	#ファイルオブジェクトのread()と同じ


pattern = re.compile(r'.*("url":.+)\,.+')	#必要な情報を取り出す

if pattern.search(data):
	data = pattern.sub(r"\1", data)
	print data

"""
python 025.py < england.txt | python 026.py | python 027.py | python 028.py | python 029.py

"url":"http://upload.wikimedia.org/wikipedia/commons/a/ae/Flag_of_the_United_Kingdom.svg"

urllib.urlencode():パーセントエンコードされた文字列に変換
					->urlopen()に適した形式にする

"""
