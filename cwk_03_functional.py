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


def score_and_rank_races_of_boat_type(data_arr, boat_type, races_data_struct):

    ##  Top level function of section 3, all others called by this.

    races_data_struct = build_data_structure(data_arr)

    races_data_struct_sec_3 = mark_final_races_by_boat_type(races_data_struct)

    all_boat_scores = build_data_structure_for_boat_results(races_data_struct_sec_3)

    final_scores_of_boat = final_rank_data(boat_type, races_data_struct_sec_3, all_boat_scores)


def build_data_structure_for_boat_results(races_data_struct):

    ##  Calls data structure setup, then fills in scores
    ##    for each boat type, sub-ordered by country.

    all_boat_scores = setup_dict_for_boat_results(10, 10)

    for key, race_data in races_data_struct.items():

        boat_type = race_data['boat']

        scores_prev = all_boat_scores[boat_type]

        scores_new = score_countries(
            race_data['results_valid'],
            race_data['results_invalid'],
            race_data['points'],
            10)

        all_boat_scores[boat_type] = \
            merge_score_dicts(scores_prev, scores_new)

    return all_boat_scores


def mark_final_races_by_boat_type(data_struct):

    ##  Iterate through all race data starting from last,
    ##    mark each last race within the data structure.

    quantity_of_races = len(data_struct)

    boat_types = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    for race_n in range(quantity_of_races, 1, -1):

        race_n_boat_type = data_struct[race_n]['boat']

        if race_n_boat_type in boat_types:

            boat_types.remove(race_n_boat_type)

            data_struct[race_n]['final_race'] = True

        else:

            data_struct[race_n]['final_race'] = False

    return data_struct


def setup_dict_for_boat_results(boat_type_quantity, country_quantity):

    ##  Setup dictionary with boat type keys,
    ##    with each boat type being assigned a sub-dictionary
    ##    for country scores.

    boat_results = {}

    template_countries = build_dict_country_scores(country_quantity)

    for j in range(1, boat_type_quantity + 1):

        boat_results[j] = template_countries.copy()

    return boat_results


def build_dict_country_scores(country_quantity):

    ##  Setup dictionary for scores for each country.

    template_countries = {}

    for i in range(1, country_quantity + 1):

        template_countries[i] = 0

    return template_countries


def score_countries(valid_entries, disqual_entries, points, country_quantity):

    ##  Take specific race data and score each country using it.

    country_scores = build_dict_country_scores(country_quantity)

    score = 1

    for entry in valid_entries:

        country_scores[entry] = score * points

        score += 1

    for entry in disqual_entries:

        country_scores[entry] = 11 * points

    return country_scores


def merge_score_dicts(scores_prev, scores_new):

    ##  Merge two dictionaries with assigned scores for each country.

    new_dict = {}

    for k, v in scores_prev.items():

        try:

            new_dict[k] = scores_prev[k] + scores_new[k]

        except:

            new_dict[k] = scores_prev[k]

    return new_dict


def final_rank_data(boat_type, races_data_struct_sec_3, all_boat_scores):

    ##  Catch the final race for a specific boat type,
    ##    adjust the scores as necessary.

    final_race = find_final_race_of_boat_type(boat_type, races_data_struct_sec_3)

    sorted_scores = sort_scores(all_boat_scores[boat_type], final_race)

    # print(sorted_scores)

    formatted_scores = format_scores(sorted_scores, all_boat_scores[boat_type])

    
def find_final_race_of_boat_type(boat_type, races_data_struct_sec_3):

    ##  Take boat type and data structure, return final race data.

    for race_n, race_n_data in races_data_struct_sec_3.items():

        if race_n_data['final_race'] == True and \
           race_n_data['boat'] == boat_type:
            
            return race_n_data

        
def sort_scores(boat_type_scores, final_race):

    ##  Take dictionary of boat type scores per country,
    ##    compare with final race.

    highest_score = 0

    for country, score in boat_type_scores.items():

        if score > highest_score:

            highest_score = score

    rank = 1

    ranks_by_country = rank_scores(boat_type_scores, highest_score)

    ranks_sorted = adjust_for_ties(boat_type_scores, ranks_by_country, final_race)

    return ranks_sorted


def rank_scores(boat_type_scores, highest_score):

    ##  Creates a new dictionary, that can be used like a linked list:
    ##    { rank: [countries] }, used to access scores from { country: score }

    rank_by_country = {}

    for rank in range(1, 11):

        rank_by_country[rank] = []

    print(boat_type_scores)

    rank = 1

    rank_iter = False

    for score_iter in range(1, highest_score + 1):

        for country, country_score in boat_type_scores.items():

            if country_score == score_iter:

                rank_iter = True

                print(country)

                rank_by_country[rank].append(country)

        if rank_iter == True:

            rank += 1

            rank_iter = False

        
    print(rank_by_country)


    return rank_by_country


def adjust_for_ties(boat_type_scores, ranks_by_country, final_race):

    ##  Iterate over the ranks by country.

    for rank, countries_arr in ranks_by_country.items():

        if len(countries_arr) > 1:

            new_order = reorder_countries(countries_arr, final_race)

            ranks_by_country[rank] = new_order

    return ranks_by_country


def reorder_countries(unsorted_countries_arr, final_race):

    ##  Iterate over the original race results, looking for specific
    ##  elements.

    sorted_countries_arr = []

    results_final_race = final_race['results_valid'] + \
        final_race['results_invalid']

    for country in results_final_race:

        if country in unsorted_countries_arr:

            sorted_countries_arr.append(country)

    return sorted_countries_arr


def format_scores(sorted_scores, boat_type_scores):

    ##  Take the processed data, fit into expected format.

    final_rank = 1

    formatted_rank_all = ""

    for rank_n, countries in sorted_scores.items():

        for country in countries:

            formatted_rank = str(country).zfill(2) + \
                str(final_rank).zfill(2) + \
                str(sorted_scores[country]).zfill(2)

            formatted_rank_all += formatted_rank

            final_rank += 1


