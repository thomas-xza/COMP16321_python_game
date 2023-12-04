#!/usr/bin/env python3


def read_file(filename="input.txt"):

    file_as_array = []

    with open(filename, encoding="utf-8") as f:

        for line in f:

            file_as_array.append(line.strip())

    return file_as_array




def specific_race_results(data_arr, boat_n, race_x):

    races_data = build_data_structures_section_2(data_arr)

    # print(races_data)

    try:

        found_data = races_data[boat_n][race_x]

    except:

        found_data = ""

    return found_data


def build_data_structures_section_2(arr):

    ##  ['0902-0701-0302-0403-08xx-0605-1006-0207-0508-0909-0910',
    ##   '0903-0801-0702-0603-05xx-0405-0306-0207-0108-1009-0910']
    ##  => { 9:
    ##          { 2: '0701-0302-0403-08xx-0605-1006-0207-0508-0909-0910'
    ##            3: '0801-0702-0603-05xx-0405-0306-0207-0108-1009-0910' }
    ##     }

    data_struct = {}

    race_results_dict = {}

    for line in arr:

        boat = extract_data('boat', line)

        race = extract_data('race', line)

        results = extract_data('results', line)

        race_results_dict = { race: results }

        # print(boat, race, results)

        data_struct[boat] = { **data_struct[boat], race_results_dict }

    # print(data_struct)

    return data_struct


def extract_data(data_type, line):

    if data_type == 'boat':

        return int(line.split()[0][0:2])

    elif data_type == 'race':

        return int(line.split()[0][2:4])

    elif data_type == 'results':

        results = line.split('-')

        results_2 = results[1:len(results)]

        results_3 = []

        for result in results_2:

            country = result[0:2]

            results_3.append(country)

        return results_2

        
