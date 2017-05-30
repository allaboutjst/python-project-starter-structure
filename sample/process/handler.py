# -*- coding: utf-8 -*-

from sample.utils.cleanup import *


class Handler(object):
    def __init__(self):
        pass

    @staticmethod
    def process_string(s):
        if s and isinstance(s, str):
            return normalize(s)

        return None
