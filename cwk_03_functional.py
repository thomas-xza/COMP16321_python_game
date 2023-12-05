#!/usr/bin/env python3


#####  SECTION 1


def read_file(filename='input.txt'):

    file_as_array = []

    with open(filename, encoding='utf-8') as f:

        for line in f:

            file_as_array.append(line.strip())

    return file_as_array


#####  SECTION 2


def specific_race_results(data_arr, race_x, boat_n):

    races_data = build_data_structure(data_arr)

    race_data = races_data[race_x]

    if race_data['boat'] == boat_n:

        return race_data['results_raw']

    else:

        return ''


def build_data_structure(arr):

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


#####  SECTION 3


def build_data_structure_for_boat_results(base_data_struct):

    data_struct_sec_3 = mark_final_races_by_boat_type(base_data_struct)

    all_boat_results = setup_dict_for_boat_results(10, 10)

    for key, race_data in base_data_struct.items():

        boat_type = race_data['boat']

        scores_prev = all_boat_results[boat_type]

        scores_new = score_countries(
            race_data['results_valid'],
            race_data['results_invalid'],
            race_data['points'],
            10)

        all_boat_results[boat_type] = \
            merge_score_dicts(scores_prev, scores_new)

    return all_boat_results


def mark_final_races_by_boat_type(data_struct):

    quantity_of_races = len(data_struct)

    boat_types = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    for race_n in range(quantity_of_races, race_n, -1):

        race_n_boat_type = data_struct['boat']

        if race_n_boat_type in boat_types:

            boat_types.remove(race_n_boat_type)

            data_struct[race_n]['final_race'] = True

        else:

            data_struct[race_n]['final_race'] = False

    print(data_struct[quantity_of_races])


def setup_dict_for_boat_results(boat_type_quantity, country_quantity):

    boat_results = {}

    template_countries = build_dict_country_scores(country_quantity)

    for j in range(1, boat_type_quantity + 1):

        boat_results[j] = template_countries.copy()

    return boat_results


def build_dict_country_scores(country_quantity):

    template_countries = {}

    for i in range(1, country_quantity + 1):

        template_countries[i] = 0

    return template_countries


def score_countries(valid_entries, disqual_entries, points, country_quantity):

    country_scores = build_dict_country_scores(country_quantity)

    score = 1

    for entry in valid_entries:

        country_scores[entry] = score * points

        score += 1

    for entry in disqual_entries:

        country_scores[entry] = 11 * points

    return country_scores


def merge_score_dicts(scores_prev, scores_new):

    new_dict = {}

    # print(scores_prev, scores_new)

    for k, v in scores_prev.items():

        try:

            new_dict[k] = scores_prev[k] + scores_new[k]

        except:

            new_dict[k] = scores_prev[k]

    return new_dict

