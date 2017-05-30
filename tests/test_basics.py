# -*- coding: utf-8 -*-
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from demo.str_process import classLv01
from demo.process.handler import Handler


class BasicTestSuite(unittest.TestCase):
    """
    Test level 1 class
    """
    def test_CalssLv01(self):
        str = classLv01.process_str("a Simple Test")
        assert(str == "a simple test")
        str = classLv01.process_str("A simple test")
        assert(str == "A SIMPLE TEST")


    """
    Test level 2 class
    """
    def test_Handler(self):
        str = Handler.process_string("a Simple Test")
        assert(str == "a simple test")
        str = Handler.process_string("A simple test")
        assert(str == "A SIMPLE TEST")


if __name__ == '__main__':
    unittest.main()
