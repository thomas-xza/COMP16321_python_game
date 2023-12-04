#!/usr/bin/env python3

import unittest

from cwk_03_functional import *


class Test_section_3(unittest.TestCase):

    
    def test_build_data_structure_for_boat_results(self):

        base_dict = setup_dict_for_boat_results(2, 5)

        expected_dict = {
            1: { 1:0,
                 2:0,
                 3:0,
                 4:0,
                 5:0 },
            2: { 1:0,
                 2:0,
                 3:0,
                 4:0,
                 5:0 }
        }

        self.assertEqual(base_dict, expected_dict)
        

    def test_process_data_for_boat_results(self):

        data_struct = {
             1: {
                 'boat': 9,
                 'points': 2,
                 'results_raw': '0701-0302-0403-08xx-0605-1006-0207-0508-0909-0110',
                 'results_valid': [7,3,4,6,10,2,5,9,1],
                 'results_invalid': [8],
             },
             2: {
                 'boat': 9,
                 'points': 1,
                 'results_raw': '0801-0702-0603-05xx-0405-0306-0207-0108-1009-0
910',
                 'results_valid': [8,7,6,4,3,2,1,10,9],
                 'results_invalid': [5],
             }
         }
        
        self.assertEqual(base_dict, expected_dict)
        

if __name__ == '__main__':
    unittest.main()
