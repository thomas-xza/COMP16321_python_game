import unittest

from cwk_03_functional import *

class Test_section_2(unittest.TestCase):

    def test_section_2_valid(self):

        file_as_arr = read_file()

        results = specific_race_results(file_as_arr, 5, 2)

        expected_results = '0101-0602-0703-0804-1005-0506-0907-0408-0209-0310'

        print(results)
                
        self.assertEqual(results, expected_results)


    def test_section_2_valid_2(self):

        file_as_arr = read_file()

    def test_section_2_extreme(self):

        file_as_arr = read_file()

        

if __name__ == '__main__':
    unittest.main()
