# -*- coding: utf-8 -*-

from sample.utils.string.case_converter import *

def normalize(s):
    if s and isinstance(s, str):
        if s[0] == s[0].upper():
            return toUpperCases(s)
        else:
            return toLowerCases(s)

    return None
