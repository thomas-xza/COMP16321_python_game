import unittest

from cwk_03_functional import *

class Test_section_1(unittest.TestCase):

    def test_section_1_valid(self):

        file_as_arr = read_file()

        first_line = "0601-0501-0702-0803-0904-0405-0306-0207-1008-0609-0110"

        self.assertEqual(file_as_arr[0], first_line)

    def test_section_2_valid(self):

        file_as_arr = read_file()

        self.assertEqual(len(file_as_arr), 34)

    def test_section_1_extreme(self):

        file_as_arr = read_file()

        self.assertEqual(file_as_arr[-1], "0202-0701-0502-0403-0204-0105-03xx-0907-10xx-0609-0810")

        

if __name__ == '__main__':
    unittest.main()
