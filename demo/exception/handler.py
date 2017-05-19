# -*- coding: utf-8 -*-

from demo.level1_2 import Level1_2
from demo.utils.level2 import Level2

class Handler(object):
    def __init__(self):
        self.level2 = Level2()
        pass

    @staticmethod
    def get_info(self):
        res = Level2.get_info()
        return "level1_2: get_info" + res
