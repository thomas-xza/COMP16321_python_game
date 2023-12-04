import unittest

from cwk_03_functional import *

class Test_section_2(unittest.TestCase):

    def test_build_data_structures_section_2(self):

         data_arr = [
             '0902-0701-0302-0403-08xx-0605-1006-0207-0508-0909-0910',
             '0901-0801-0702-0603-05xx-0405-0306-0207-0108-1009-0910'
         ]

         data_struct = build_data_structures_section_2(data_arr)

         print(data_struct)

         expected_data_struct = {
             1: {
                 "boat": 9,
                 "points": 1,
                 "results_raw": '0701-0302-0403-08xx-0605-1006-0207-0508-0909-0910',
                 "results_valid": [7,3,4,6,10,2,5,9,1],
                 "results_invalid": [8],
             },
             2: {
                 "boat": 9,
                 "points": 1,
                 "results_raw": '0801-0702-0603-05xx-0405-0306-0207-0108-1009-0910',
                 "results_valid": [8,7,6,4,3,2,1,10,9],
                 "results_invalid": [5],
             }
         }
         
         self.assertEqual(data_struct, expected_data_struct)

    # def test_section_2_valid(self):

    #     file_as_arr = read_file()

    #     results = specific_race_results(file_as_arr, 5, 2)

    #     expected_results = '0101-0602-0703-0804-1005-0506-0907-0408-0209-0310'

    #     print(results)
                
    #     self.assertEqual(results, expected_results)


    # def test_section_2_valid_2(self):

    #     file_as_arr = read_file()
        

    # def test_section_2_extreme(self):

    #     file_as_arr = read_file()

        

if __name__ == '__main__':
    unittest.main()
