#062.py
# -*- coding:utf-8 -*-

import plyvel

def main():
	count = 0
	db = plyvel.DB("/tmp/area.db", create_if_missing=True)
	for k, v in db:
		if v == "Japan":
			count += 1
		else:
			pass
	return count

if __name__ == "__main__":
	print main()

"""
python 062.py

21946
"""
