# coding:utf-8

import unittest
from demo import Demo

class DemoTestCase(unittest.TestCase):
    def test_demo(self):
        self.assertEqual(Demo().demo1(1,23), 24)
        
if __name__ == '__main__':
    unittest.main()