#!/usr/bin/env python3

import unittest

from cwk_03_functional import *


class Test_section_2(unittest.TestCase):

    
    def test_specific_race_results_valid(self):

        data_arr = read_file()

        results = specific_race_results(data_arr, 20, 4)

        expected_results = \
        '0201-0402-0603-0504-0905-0306-0707-0108-0809-1010'

        self.assertEqual(results, expected_results)


    def test_specific_race_results_invalid(self):

        data_arr = read_file()

        results = specific_race_results(data_arr, 20, 5)

        expected_results = ''

        self.assertEqual(results, expected_results)


    def test_process_data_valid_1(self):

        results = process_data(
            'results_valid',
            '0701-0302-0403-0808-0605-1006-0207-0508-0909-0110'
        )

        expected_results = [7,3,4,8,6,10,2,5,9,1]

        self.assertEqual(results, expected_results)


    def test_process_data_valid_2(self):

        results = process_data(
            'results_invalid',
            '0801-0702-0603-05xx-0405-0306-0207-0108-1009-0910'
        )

        expected_results = [5]

        self.assertEqual(results, expected_results)

        
    def test_process_data_extreme_1(self):

        results_v = process_data(
            'results_invalid',
            '08xx-07xx-06xx-05xx-04xx-03xx-02xx-01xx-10xx-09xx'
        )

        results_inv = process_data(
            'results_valid',
            '08xx-07xx-06xx-05xx-04xx-03xx-02xx-01xx-10xx-09xx'
        )

        expected_results = [8,7,6,5,4,3,2,1,10,9]

        self.assertEqual(results_v, expected_results)
        self.assertEqual(results_inv, [])


    def test_build_data_structures_section_2(self):

         data_arr = [
             '0902-0701-0302-0403-08xx-0605-1006-0207-0508-0909-0110',
             '0901-0801-0702-0603-05xx-0405-0306-0207-0108-1009-0910'
         ]

         data_struct = build_data_structure(data_arr)

         # print(data_struct)

         expected_data_struct = {
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
                 'results_raw': '0801-0702-0603-05xx-0405-0306-0207-0108-1009-0910',
                 'results_valid': [8,7,6,4,3,2,1,10,9],
                 'results_invalid': [5],
             }
         }
         
         self.assertEqual(data_struct, expected_data_struct)
        

if __name__ == '__main__':
    unittest.main()
