# -*- coding: utf-8 -*-
import os
import sys
#sys.path.append('demo')
# testfolder = os.path.abspath(os.path.dirname(__file__))
# project_root = os.path.abspath(os.path.join(testfolder, r"..\.."))
# sys.path.append(project_root)

from mypkg import Level1_2

def test_level_1():
    str=Level1_2.get_info()
    print(str)

if __name__ == '__main__':
    test_level_1()