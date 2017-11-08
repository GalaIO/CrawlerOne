# -*- encoding: utf-8 -*-
__author__ = 'GalaIO'

def deal(content):
    print content
    f = open("1.jpg", 'wb')
    f.write(content[1])
    f.flush()
    f.close()
    return []