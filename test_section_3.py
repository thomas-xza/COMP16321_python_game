#!/usr/bin/env python3

import unittest

from cwk_03_functional import *


class Test_section_3(unittest.TestCase):

    
    def test_build_data_structure_for_boat_results(self):

        data_arr = read_file()

        # base_data_struct = build_data_structure(data_arr)

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
        

if __name__ == '__main__':
    unittest.main()
