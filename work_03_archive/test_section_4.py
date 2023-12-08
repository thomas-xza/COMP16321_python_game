#!/usr/bin/env python3

import unittest

from cwk_03_functional import *


class Test_section_3(unittest.TestCase):

    maxDiff = None
    
    def test_find_worst_scores_1(self):
    
        data = {
            1: {
                'boat': 9,
                'points': 2,
                'results_raw': '0701-0302-0403-08xx-0605-1006-0207-0508-0909-0110',
                'results_valid': [7,3,4,6,10,2,5,9,1],
                'results_invalid': [8]
            },
            2: {
                'boat': 9,
                'points': 2,
                'results_raw': '0801-0702-0603-05xx-0405-0306-0207-0108-1009-0910',
                'results_valid': [8,7,6,4,3,2,1,10,9],
                'results_invalid': [5]
            },
            3: {
                'boat': 9,
                'points': 2,
                'results_raw': '0801-0702-0603-05xx-0405-0306-0207-0108-1009-0910',
                'results_valid': [8,7,6,4,3,2,1,10,9],
                'results_invalid': [5]
            }
        }

        expected_output_2 = {
            1: 9*-2,
            2: 6*-2,
            3: 5*-2,
            4: 4*-2,
            5: 11*-2,
            6: 4*-2,
            7: 2*-2,
            8: 11*-2,
            9: 9*-2,
            10: 8*-2
        }

        two_point_scores_del = derive_worst_scores(data, 9, 2)

        self.assertEqual(two_point_scores_del, expected_output_2)
        
        
    def test_find_worst_scores_2(self):
    
        data = {
            1: {
                'boat': 9,
                'points': 1,
                'results_raw': '0701-0302-0403-08xx-0605-1006-0207-0508-0909-0110',
                'results_valid': [7,3,4,6,10,2,5,9,1],
                'results_invalid': [8]
            }
        }

        expected_output_2 = {
            1: 0,
            2: 0,
            3: 0,
            4: 0,
            5: 0,
            6: 0,
            7: 0,
            8: 0,
            9: 0,
            10: 0
        }

        two_point_scores_del = derive_worst_scores(data, 9, 1)

        self.assertEqual(two_point_scores_del, expected_output_2)

        
    def test_score_and_rank_races_of_boat_type(self):

        races_data_struct = {
            1: {
                'boat': 9,
                'points': 2,
                'results_raw': '0701-0302-0403-08xx-0605-1006-0207-0508-0909-0110',
                'results_valid': [7,3,4,6,10,2,5,9,1],
                'results_invalid': [8]
            },
            2: {
                'boat': 9,
                'points': 2,
                'results_raw': '0801-0702-0603-05xx-0405-0306-0207-0108-1009-0910',
                'results_valid': [8,7,6,4,3,2,1,10,9],
                'results_invalid': [5]
            },
            3: {
                'boat': 9,
                'points': 2,
                'results_raw': '0801-0702-0603-05xx-0405-0306-0207-0108-1009-0910',
                'results_valid': [8,7,6,4,3,2,1,10,9],
                'results_invalid': [5]
            }
        }

        boat_type = 9
    
        one_point_scores_del = derive_worst_scores(races_data_struct, boat_type, 1)

        two_point_scores_del = derive_worst_scores(races_data_struct, boat_type, 2)

        races_data_struct_sec_3 = mark_final_races_by_boat_type(races_data_struct)

        all_boat_scores = build_data_structure_for_boat_results(races_data_struct_sec_3)

        print(all_boat_scores[boat_type])

        all_boat_scores[boat_type] = merge_score_dicts(all_boat_scores[boat_type], one_point_scores_del)

        all_boat_scores[boat_type] = merge_score_dicts(all_boat_scores[boat_type], two_point_scores_del)

        # print(all_boat_scores[boat_type])

        expected_output = {
            1: 46 + 9*-2,
            2: 36 + 6*-2,
            3: 24 + 5*-2,
            4: 22 + 4*-2,
            5: 58 + 11*-2,
            6: 20 + 4*-2,
            7: 10 + 2*-2,
            8: 26 + 11*-2,
            9: 52 + 9*-2,
            10: 42 + 8*-2
        }

        self.assertEqual(all_boat_scores[boat_type], expected_output)
        

if __name__ == '__main__':
    unittest.main()
