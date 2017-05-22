# -*- coding: utf-8 -*-

from demo.process.handler import *


class classLv01(object):
    """
    this class is depended on multiple inner class/methods
    """
    def __init__(self):
        pass

    @staticmethod
    def process_str(s):
        if s and isinstance(s, str):
            handler = Handler()
            return handler.process_string(s)

        return "None"
