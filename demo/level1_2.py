# -*- coding: utf-8 -*-

from .level1_1 import Level1_1

class Level1_2(object):
    def __init__(self):
        self.level1_obj = Level1_1()
        pass

    @staticmethod
    def get_info():
        res = Level1_1.get_info()
        return "level1_2: get_info" + res
