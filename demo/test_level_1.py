# -*- coding: utf-8 -*-
# from __future__ import absolute_import

from demo.level1_2 import Level1_2
#mport imp
#module = imp.load_source('demo.Level1_2', '.')

def test():
    level1_2 = Level1_2()
    str=level1_2.get_info()
    print(str)

if __name__ == '__main__' and __package__ is None:
    __package__ = 'pkg'
    test()