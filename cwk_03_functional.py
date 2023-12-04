#!/usr/bin/env python3


#####  SECTION 1


def read_file(filename='input.txt'):

    file_as_array = []

    with open(filename, encoding='utf-8') as f:

        for line in f:

            file_as_array.append(line.strip())

    return file_as_array



#####  SECTION 2


def specific_race_results(data_arr, boat_n, race_x):

    races_data = build_data_structure(data_arr)

    # print(races_data)

    try:

        found_data = races_data[boat_n][race_x]

    except:

        found_data = ''

    return found_data


def build_data_structure(arr):

    ##  ['0902-0701-0302-0403-08xx-0605-1006-0207-0508-0909-0110',
    ##   '0901-0801-0702-0603-05xx-0405-0306-0207-0108-1009-0910']
    ##  => {
    ##    data_struct[race_n] = {
    ##       1: {
    ##          'boat': 9,
    ##          'points': 1,
    ##          'results_raw': '0701-0302-0403-08xx-0605-1006-0207-0508-0909-0910',
    ##          'results_valid': [7,3,4,6,10,2,5,9,1],
    ##          'results_invalid': [8],
    ##          },
    ##       2: {
    ##          'boat': 9,
    ##          'points': 1,
    ##          'results_raw': '0801-0702-0603-05xx-0405-0306-0207-0108-1009-0910',
    ##          'results_valid': [8,7,6,4,3,2,1,10,9],
    ##          'results_invalid': [5],
    ##          }
    ##     }

    data_struct = {}

    race_n = 0

    for line in arr:

        race_n += 1

        results_raw =  extract_data('results_raw', line)
        
        data_struct[race_n] = {
            'boat': extract_data('boat', line),
            'points': extract_data('points', line),
            'results_raw': results_raw,
            'results_valid': process_data('results_valid', results_raw),
            'results_invalid': process_data('results_invalid', results_raw)
        }

    return data_struct


def extract_data(data_type, line):

    if data_type == 'boat':

        return int(line.split()[0][0:2])

    elif data_type == 'points':

        return int(line.split()[0][2:4])

    elif data_type == 'results_raw':

        results = line.split('-')

        results_2 = '-'.join(results[1:len(results)])

        return results_2

        
def process_data(process_type, results_raw):

    results_arr = results_raw.split('-')

    results_valid = []

    results_invalid = []

    for result in results_arr:

        country = int(result[0:2])

        if 'xx' in result:

            results_invalid.append(country)

        else:

            results_valid.append(country)
            

    if process_type == 'results_valid':

        return results_valid

    elif process_type == 'results_invalid':

        return results_invalid
