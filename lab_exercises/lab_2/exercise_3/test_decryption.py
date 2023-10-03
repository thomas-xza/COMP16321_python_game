#!/usr/bin/env python3

import unittest

from decryption import *

class TestStringMethods(unittest.TestCase):

    def test_1(self):
        self.assertEqual(decryption("ILSBMVQELK"), "LOVEPYTHON")

    def test_2(self):
        self.assertEqual(decryption("ILSBRLJ"), "LOVEUOM")

    def test_3(self):
        self.assertEqual(decryption("CRIILCILSB"), "FULLOFLOVE")

if __name__ == '__main__':
    unittest.main()
