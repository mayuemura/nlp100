#061.py
# -*- coding:utf-8 -*-

import plyvel
import sys

def main():
	db = plyvel.DB("/tmp/area.db", create_if_missing=True)
	query = sys.argv[1]
	print db.get(query)

if __name__ == "__main__":
	main()

"""
python 061.py "Al Street"
United States

python 061.py "Love .45"
None
"""
