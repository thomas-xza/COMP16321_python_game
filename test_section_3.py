#!/usr/bin/env python3

import unittest

from cwk_03_functional import *


class Test_section_3(unittest.TestCase):

    maxDiff = None
    
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

        
    def test_score_countries(self):
    
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
                'points': 1,
                'results_raw': '0801-0702-0603-05xx-0405-0306-0207-0108-1009-0910',
                'results_valid': [8,7,6,4,3,2,1,10,9],
                'results_invalid': [5]
            }
        }

        expected_output = {
            1: 9*2 + 7,
            2: 6*2 + 6,
            3: 2*2 + 5,
            4: 3*2 + 4,
            5: 7*2 + 11,
            6: 4*2 + 3,
            7: 1*2 + 2,
            8: 11*2 + 1,
            9: 8*2 + 9,
            10: 5*2 + 8
        }

        scores_a = score_countries(data[1]['results_valid'],
                                   data[1]['results_invalid'],
                                   data[1]['points'],
                                   10)

        scores_b = score_countries(data[2]['results_valid'],
                                   data[2]['results_invalid'],
                                   data[2]['points'],
                                   10)

        merged_scores = merge_score_dicts(scores_a, scores_b)

        self.assertEqual(merged_scores, expected_output)
        
        
    def test_process_data_for_boat_results(self):

        data_struct = {
            1: {
                'boat': 9,
                'points': 1,
                'results_raw': '0701-0302-0403-08xx-0605-1006-0207-0508-0909-0110',
                'results_valid': [7,3,4,6,10,2,5,9,1],
                'results_invalid': [8],
                'final_race': False
                
            },
            2: {
                'boat': 8,
                'points': 1,
                'results_raw': '0301-0202-0103-10xx-0905-0806-0707-0608-0509-0410',
                'results_valid': [3,2,1,9,8,7,6,5,4],
                'results_invalid': [10],
                'final_race': True
            }            
        }

        boat_scores = {

            }

        boat_results = build_data_structure_for_boat_results(data_struct)
        
        expected_output = {
            8: {
                1: 3,
                2: 2,
                3: 1,
                4: 9,
                5: 8,
                6: 7,
                7: 6,
                8: 5,
                9: 4,
                10: 11                
                },
            9: {
                1: 9*2 + 7,
                2: 6*2 + 6,
                3: 2*2 + 5,
                4: 3*2 + 4,
                5: 7*2 + 11,
                6: 4*2 + 3,
                7: 1*2 + 2,
                8: 11*2 + 1,
                9: 8*2 + 9,
                10: 5*2 + 8
                }
        }

        self.assertEqual(boat_results[9], expected_output[9])
        self.assertEqual(boat_results[8], expected_output[8])

        
    def test_final_rank_data(self):

        data_struct = {
            1: {
                'boat': 9,
                'points': 1,
                'results_raw': '0701-0302-0403-08xx-0605-1006-0207-0508-0909-0110',
                'results_valid': [7,3,4,6,10,2,5,9,1],
                'results_invalid': [8],
                'final_race': False
                
            },
            2: {
                'boat': 8,
                'points': 1,
                'results_raw': '01xx-02xx-03xx-0404-0505-0606-0707-0808-0909-10xx',
                'results_valid': [2,4,5,6,7,8,9],
                'results_invalid': [1,2,3,10],
                'final_race': True
            },
            3: {
                'boat': 8,
                'points': 1,
                'results_raw': '1001-0902-0803-07xx-0605-0506-0407-0308-02xx-01xx',
                'results_valid': [10,9,8,6,5,4,3],
                'results_invalid': [7,2,1],
                'final_race': True
            }
        }

        all_boat_scores = build_data_structure_for_boat_results(data_struct)

        output = final_rank_data(8, races_data_struct_sec_3, all_boat_scores)
        

if __name__ == '__main__':
    unittest.main()
