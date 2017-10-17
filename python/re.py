# !/usr/bin/python
# -*- coding:UTF-8 -*-
import re
__author__ = 'shaoyong_li'


def main():
    p = re.compile("\(\S{2,3}\)")
    content = '''(sdfasdfa)sdfkasldfjsdlfjsldfjs;ldfkjsldkfjs;ldkfjs;d90(ab)(abc) '''
    ret = p.search(content)
    print ret.group()

# print(b)
if __name__ == "__main__":
    main()
