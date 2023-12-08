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


def score_and_rank_races_of_boat_type(data_arr, boat_type):

    ##  Top level function of section 3, all others called by this.

    races_data_struct = build_data_structure(data_arr)

    races_data_struct_sec_3 = mark_final_races_by_boat_type(races_data_struct)

    # print(races_data_struct_sec_3)

    all_boat_scores = build_data_structure_for_boat_results(races_data_struct_sec_3)

    final_scores_of_boat = final_rank_data(boat_type, races_data_struct_sec_3, all_boat_scores)

    return final_scores_of_boat


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

    # print(data_struct)

    for race_n in range(quantity_of_races, 0, -1):

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

    formatted_scores = format_scores(sorted_scores, all_boat_scores[boat_type])

    return formatted_scores

    
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

    # print(ranks_by_country)

    ranks_sorted = adjust_for_ties(boat_type_scores, ranks_by_country, final_race)

    # print(ranks_sorted)

    return ranks_sorted


def rank_scores(boat_type_scores, highest_score):

    ##  Creates a new dictionary, that can be used like a linked list:
    ##    { rank: [countries] }, used to access scores from { country: score }

    rank_by_country = {}

    for rank in range(1, 11):

        rank_by_country[rank] = []

    rank = 1

    rank_iter = False

    for score_iter in range(1, highest_score + 1):

        for country, country_score in boat_type_scores.items():

            if country_score == score_iter:

                rank_iter = True

                # print(country)

                rank_by_country[rank].append(country)

        if rank_iter == True:

            rank += 1

            rank_iter = False
            
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

    # print(results_final_race)

    for country in results_final_race:

        if country in unsorted_countries_arr:

            sorted_countries_arr.append(country)

    return sorted_countries_arr


def format_scores(sorted_scores, boat_type_scores):

    ##  Take the processed data, fit into expected format.

    final_rank = 1

    formatted_rank_all = []

    for rank_n, countries in sorted_scores.items():

        for country in countries:

            formatted_rank = str(country).zfill(2) + "-" + \
                str(final_rank).zfill(2) + "-" + \
                str(boat_type_scores[country]).zfill(2)

            formatted_rank_all.append(formatted_rank)

            final_rank += 1

    formatted_rank_all_str = ", ".join(formatted_rank_all)

    return formatted_rank_all_str


#####  SECTION 4


def score_and_rank_races_of_boat_type(data_arr, boat_type):

    ##  Top level function of section 4, all others called by this.

    ##  This was written before reading:
    ##    Blackboard discussion forum > Thread: Section 4 Part a
    ##  So, no idea if the below will be what is expected, too late to change.

    races_data_struct = build_data_structure(data_arr)

    one_point_scores_del = derive_worst_scores(races_data_struct, boat_type, 1)

    two_point_scores_del = derive_worst_scores(races_data_struct, boat_type, 2)

    races_data_struct_sec_3 = mark_final_races_by_boat_type(races_data_struct)

    all_boat_scores = build_data_structure_for_boat_results(races_data_struct_sec_3)
    
    all_boat_scores[boat_type] = merge_score_dicts(all_boat_scores[boat_type], one_point_scores_del)
    
    all_boat_scores[boat_type] = merge_score_dicts(all_boat_scores[boat_type], two_point_scores_del)
    
    final_scores_of_boat = final_rank_data(boat_type, races_data_struct_sec_3, all_boat_scores)

    return final_scores_of_boat


def derive_worst_scores(races_data_struct, boat_type, point_type):

    quantity = 0

    blank_country_score_dict = build_dict_country_scores(10)
    
    worst_scores = blank_country_score_dict.copy()

    for race_n, race_data in races_data_struct.items():

        if race_data['boat'] == boat_type and \
           race_data['points'] == point_type:

            quantity += 1

            country_race_scores = score_countries(race_data['results_valid'],
                                         race_data['results_invalid'],
                                         race_data['points'],
                                         10)

            worst_scores = find_worst_scores(country_race_scores, worst_scores)

    if quantity <= 2:

        worst_scores = blank_country_score_dict.copy()

    else:

        ##  Allows the merge_dicts() function to be used later.

        worst_scores = negate_dict_values(worst_scores)

    return worst_scores


def find_worst_scores(country_race_scores, worst_scores):

    for country, race_score in country_race_scores.items():

        if worst_scores[country] < race_score:

            worst_scores[country] = race_score

    return worst_scores


def negate_dict_values(dict_data):

    new_dict = {}

    for key, value in dict_data.items():

        new_dict[key] = value * -1

    return new_dict


#####  SECTION 5


def medal_scores(data_arr, boat_type):

    ##  Top level function of section 5.

    races_data_struct = build_data_structure(data_arr)

    valid_boat_types = find_boat_types_within_input(races_data_struct)

    medals_data_template = build_medals_data_struct()

    medals_data = derive_medals_data(races_data_struct, valid_boat_types, medals_data_template)

    sorted_medal_scores = sort_medals_data(medals_data)

    ##  Formatting should've been more separate, in section 4, that was a bug.
    
    medals_data_output = format_medal_scores(sorted_medal_scores)

    return medals_data_output


def find_boat_types_within_input(races_data_struct):

    ##  Take race data and return which boat types are within it.

    found_boat_types = []

    for race_n, race_data in races_data_struct.items():

        if race_data['boat'] not in found_boat_types:

            found_boat_types.append(race_data['boat'])

    return found_boat_types


def build_medals_data_struct():

    ##  Create data structure for medals of each country.

    medals_data_struct = {}

    for country in range(1, 10+1):

        medals_data_struct[country] = [0,0,0]

    return medals_data_struct


def derive_medals_data(races_data_struct, valid_boat_types, medals_data):

    ##  Iterate through the boat types, eventually return medals data.
    
    for boat_type in valid_boat_types:

        boat_type_final_ranks = derive_final_ranks(races_data_struct, boat_type)

        top_three = find_top_three_countries(boat_type_final_ranks)

        medals_data = add_to_scores(medals_data, top_three)

    return medals_data


def find_top_three_countries(boat_type_final_ranks):

    ##  Take race results, fully sorted including discards, extract top 3.

    all_countries_ranked = []

    for rank, country in boat_type_final_ranks.items():

        all_countries_ranked.extend(country)

    top_three = all_countries_ranked[0:3]

    return top_three


def add_to_scores(medals_data, top_three):

    ##  Add medals of boat type to all medals data.

    medal_type = 0

    for medal_country in top_three:

        medals_data[medal_country][medal_type] += 1

        medal_type += 1

    return medals_data


def sort_medals_data(medals_data):

    medals_data_arrs = convert_to_medal_arrays(medals_data)

    medals_sorted = sorted(medals_data_arrs, key=lambda set: set[4])

    ##  TO DO: write perfect sort function via recursion & sorted() etc...

    # medals_sorted = recurse_sort_set_by_attribute(set_to_sort, target)

    medals_sorted_rev = medals_sorted.reverse()

    return medals_sorted_rev


def recurse_sort_set_by_attribute(set_to_sort, target):

    ##  There is some way to use sorted() with recursive calls...
    ##    But not familiar enough with recursion to design algo in time!

    next_target = find_next_target(target)

    set_to_sort = sorted(set_to_sort, key=lambda set: set[target])

    if next_target == -1 or len(set_to_sort) == 1:

        return set_to_sort

    output_set = []

    for n in range(1000000):

        subset_to_sort = []

        for country_set in set_to_sort:

            if country_set[target] == n:

                subset_to_sort.append(country_set)

        output_set.extend(recurse_sort_set_by_attribute(subset_to_sort, next_target))

    return output_set


def find_next_target(target):

    if target == 4:

        return 1

    elif target == 1:

        return 2

    elif target == 2:

        return 3

    elif target == 3:

        return 0

    else:

        return -1    

    
def find_all_with(data, target, value):

    found = []

    for score_set in data:

        if score_set[target] == value:

            found.append(score_set)

    return found


def sane_print(scores):

    for score in scores:

        print(score)


def convert_to_medal_arrays(medals_data):

    ##  Convert to arrays, for sorting.

    medals_data_out = []

    for country, medal_data in medals_data.items():

        medal_score = medal_data[0] * 3 + \
            medal_data[1] * 2 + \
            medal_data[2] * 1

        medal_data_arr = [country,
                          medal_data[0],
                          medal_data[1],
                          medal_data[2],
                          medal_score]
                          
        medals_data_out.append(medal_data_arr)

    return medals_data_out


def format_medal_scores(medals_data):

    ##  Format medal data for expected output.

    ##  Brief holy F detour:
    ##    https://duckduckgo.com/?q=albino+indian&t=h_&iar=images&iax=images&ia=images

    medals_data_str_arr = []

    for medal_data in medals_data:

        medal_data_zeroed = []

        for data in medal_data:

            medal_data_zeroed.append(str(data).zfill(2))

        medals_data_str_arr.append("-".join(medal_data_zeroed))

    medals_data_str = ", ".join(medals_data_str_arr)

    return medals_data_str
    

def derive_final_ranks(races_data_struct, boat_type):

    ##  Big copy of section 4, but without the formatting
    ##    part. Really, section 4 function should instead be reworked
    ##    and called, so the formatting function of the data is less
    ##    deep (bad move), but not enough time to risk refactor etc.

    one_point_scores_del = derive_worst_scores(races_data_struct, boat_type, 1)

    two_point_scores_del = derive_worst_scores(races_data_struct, boat_type, 2)

    races_data_struct_sec_3 = mark_final_races_by_boat_type(races_data_struct)

    all_boat_scores = build_data_structure_for_boat_results(races_data_struct_sec_3)
    
    all_boat_scores[boat_type] = merge_score_dicts(all_boat_scores[boat_type], one_point_scores_del)
    
    all_boat_scores[boat_type] = merge_score_dicts(all_boat_scores[boat_type], two_point_scores_del)
    
    final_race = find_final_race_of_boat_type(boat_type, races_data_struct_sec_3)

    sorted_scores = sort_scores(all_boat_scores[boat_type], final_race)

    return sorted_scores
