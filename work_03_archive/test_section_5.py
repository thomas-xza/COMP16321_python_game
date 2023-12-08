#!/usr/bin/env python3

import unittest

import random

from cwk_03_functional import *


class Test_section_3(unittest.TestCase):

    maxDiff = None
    
    def test_overall_medal_data_1(self):

        races_data_struct = {
            1: {
                'boat': 9,
                'points': 2,
                'results_raw': '0701-0302-0403-08xx-0605-1006-0207-0508-0909-0110',
                'results_valid': [8,7,6,4,3,2,1,10,9],
                'results_invalid': [5]
            },
            2: {
                'boat': 9,
                'points': 2,
                'results_raw': '0701-0302-0403-08xx-0605-1006-0207-0508-0909-0110',
                'results_valid': [8,7,6,4,3,2,1,10,9],
                'results_invalid': [5]
            },
            3: {
                'boat': 9,
                'points': 2,
                'results_raw': '0701-0302-0403-08xx-0605-1006-0207-0508-0909-0110',
                'results_valid': [8,7,6,4,3,2,1,10,9],
                'results_invalid': [5]
            },
            4: {
                'boat': 8,
                'points': 2,
                'results_raw': '0801-0702-0603-05xx-0405-0306-0207-0108-1009-0910',
                'results_valid': [3,2,1,8,7,6,4,10,9],
                'results_invalid': [5]
            },
            5: {
                'boat': 8,
                'points': 2,
                'results_raw': '0801-0702-0603-05xx-0405-0306-0207-0108-1009-0910',
                'results_valid': [3,2,1,8,7,6,4,10,9],
                'results_invalid': [5]
            },
            6: {
                'boat': 8,
                'points': 2,
                'results_raw': '0801-0702-0603-05xx-0405-0306-0207-0108-1009-0910',
                'results_valid': [3,2,1,8,7,6,4,10,9],
                'results_invalid': [5]
            },
            7: {
                'boat': 7,
                'points': 2,
                'results_raw': '0801-0702-0603-05xx-0405-0306-0207-0108-1009-0910',
                'results_valid': [10,9,4,3,2,1,8,7,6],
                'results_invalid': [5]
            },
            8: {
                'boat': 7,
                'points': 2,
                'results_raw': '0801-0702-0603-05xx-0405-0306-0207-0108-1009-0910',
                'results_valid': [10,9,4,3,2,1,8,7,6],
                'results_invalid': [5]
            },
            9: {
                'boat': 7,
                'points': 2,
                'results_raw': '0801-0702-0603-05xx-0405-0306-0207-0108-1009-0910',
                'results_valid': [10,9,4,3,2,1,8,7,6],
                'results_invalid': [5]
            }

        }

        valid_boat_types = find_boat_types_within_input(races_data_struct)

        medals_data_template = build_medals_data_struct()

        medals_data = derive_medals_data(races_data_struct, valid_boat_types, medals_data_template)

        print(medals_data)
    
        expected_output = {
            1: [0,0,1],
            2: [0,1,0],
            3: [1,0,0],
            4: [0,0,1],
            5: [0,0,0],
            6: [0,0,1],
            7: [0,1,0],
            8: [1,0,0],
            9: [0,1,0],
            10: [1,0,0]
        }

        self.assertEqual(medals_data, expected_output)
        

    def test_overall_medal_data_2(self):

        races_data_struct = {
            1: {
                'boat': 8,
                'points': 1,
                'results_raw': '0701-0302-0403-08xx-0605-1006-0207-0508-0909-0110',
                'results_valid': [8,7,6,4,3,2,1,10,9],
                'results_invalid': [5]
            }
        }

        valid_boat_types = find_boat_types_within_input(races_data_struct)

        medals_data_template = build_medals_data_struct()

        medals_data = derive_medals_data(races_data_struct, valid_boat_types, medals_data_template)
    
        expected_output = {
            1: [0,0,0],
            2: [0,0,0],
            3: [0,0,0],
            4: [0,0,0],
            5: [0,0,0],
            6: [0,0,1],
            7: [0,1,0],
            8: [1,0,0],
            9: [0,0,0],
            10: [0,0,0]
        }

        self.assertEqual(medals_data, expected_output)
        

    def test_medal_data_formatting_1(self):

       medals_data_arrs = [
           [10, 0, 0, 0, 0],
           [2, 20, 0, 0, 60],
           [3, 17, 0, 4, 55],
           [7, 12, 0, 0, 36],
           [6, 16, 0, 0, 48],
           [9, 8, 0, 0, 24],
           [5, 16, 0, 0, 48],
           [8, 10, 0, 0, 30],
           [4, 18, 0, 0, 54],
           [1, 20, 1, 0, 62]
       ]

       expected_output = "01-20-01-00-62"

       valid = False

       medals_sorted_rev = sorted(medals_data_arrs, key=lambda set: set[4])

       medals_sorted_rev.reverse()

       print(medals_sorted_rev)

       output = format_medal_scores(medals_sorted_rev)

       print(output)

       if expected_output in output:

           valid = True

           print(output)

       self.assertTrue(valid)

       
def test_medal_data_sorting_1(self):

       medals_input = [
           [10, 0, 0, 0, 0],
           [2, 20, 0, 0, 60],
           [3, 17, 0, 4, 55],
           [7, 12, 0, 0, 36],
           [6, 16, 0, 0, 48],
           [9, 8, 0, 0, 24],
           [5, 16, 0, 0, 48],
           [8, 10, 0, 0, 30],
           [4, 18, 0, 0, 54],
           [1, 20, 1, 0, 62]
       ]

       expected_output = [
           [ 1, 20, 1, 0, 62 ],
           [ 2, 20, 0, 0, 60 ],
           [ 3, 17, 0, 4, 55 ],
           [ 4, 18, 0, 0, 54 ],
           [ 5, 16, 0, 0, 48 ],
           [ 6, 16, 0, 0, 48 ],
           [ 7, 12, 0, 0, 36 ],
           [ 8, 10, 0, 0, 30 ],
           [ 9,  8, 0, 0, 24 ],
           [ 10, 0, 0, 0,  0 ]
       ]

       output = recurse_sort_set_by_attribute(medals_input, 4)

       self.assertEqual(output, expected_output)

        
if __name__ == '__main__':
    unittest.main()
