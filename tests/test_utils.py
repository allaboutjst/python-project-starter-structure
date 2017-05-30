# -*- coding: utf-8 -*-
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from demo.utils.string.case_converter import toLowerCases, toUpperCases


class BasicTestSuite(unittest.TestCase):
    """
    Test demo.utils.string.case_converter
    """
    def testCaseConverter(self):
        str = toLowerCases("a Simple Test")
        assert(str == "a simple test")
        str = toUpperCases("a Simple Test")
        assert(str == "A SIMPLE TEST")

if __name__ == '__main__':
    unittest.main()
