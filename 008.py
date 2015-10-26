# -*- coding: utf-8 -*-

import sys

def cipher(s):
    l = []
    for c in s:
        char_code = ord(c)
        if 97 <= char_code <= 122:
            l.append(chr(219-char_code))
        else:
            l.append(c)
    return l

def main():
    print ''.join(cipher(u"ほげほげugug"))

if __name__ == '__main__':
    main()
			
