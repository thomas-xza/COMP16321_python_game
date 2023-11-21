#!/usr/bin/env python3

import json
import random

def handle_state_definitions(data):

    print("tick...")

    state = data['next_state']
 
    if state == 'play':

        data['timerDelay'] = data['prev_timer_delay']
        data['random_n'] = random.randrange(1, data['max_random'])

        if data['score'] != 0:
            data['score'] -= 1

    elif state == 'pause' or state == 'bossmode':

        ##  We can't actually pause with this CMU template, because
        ##    setting the timer high can't be interrupted.

        ##  So, next option is to allow game to keep running in
        ##    background, and hide and restore status.

        data['level_pause'] = data['level']

    elif state == 'unpause':

        data['level'] = data['level_pause']

        data['next_state'] = 'play'

    elif state == 'highscores_input':

        data = handle_highscores_input_state(data)

    elif state == 'highscores_display':

        data = handle_highscores_display_state(data)

    elif state == 'level_up':

        data = handle_level_up_state(data)

    elif state == 'save':

        with open('savefile.txt', 'w', encoding="utf-8") as f:
            f.write(f"{data['level']},{data['score']}")

        data['next_state'] = 'play'

    data['state'] = data['next_state']

    return data


def handle_highscores_input_state(data):

    ##  Speed up the clock so user input doesn't lag.

    data['timerDelay'] = 50

    user_input_str = data['highscore_new_entry']

    if len(user_input_str) >= 3:

        ##  Valid input received, so load highscores, update, write.

        try:

            with open('highscores.json', 'r', encoding="utf-8") as f:
                data['highscores'] = json.load(f.read().strip())

        except:

            data['highscores'] = {}

        data['highscores'][user_input_str[0:3]] = data['score']
        
        with open('highscores.json', 'w', encoding="utf-8") as f:
            f.write(json.dump(data['highscores']))

        ##  Revert the clock by simulating a level up.

        data = load_level(data, data['level'] - 1)

        ##  Ready to display highscores.

        data['next_state'] = 'highscores_display'

    return data


def handle_highscores_display_state(data):

    ##  No data manipulation occurs in this state.

    pass


def handle_level_up_state(data):

    if data['level_up_src'] == 'cheat':

        data = handle_level_up_via_cheat(data)

    elif data['level_up_src'] == 'load':

        data = handle_level_up_via_load(data)

    elif data['level_up_src'] == 'win':

        data = load_level(data, data['level'] + 1)

    return data


def handle_level_up_via_cheat(data):

    presses = data['cheat_presses']

    if presses == 10:

        data = load_level(data, 100)
        data['cheat_presses'] = 0
        data['score'] += 1000000

    else:

        data['cheat_presses'] += 1

    return data
    

def handle_level_up_via_load(data)

    try:

        with open('savefile.txt', encoding="utf-8") as f:
            save_file = int(f.read().strip())

        saved_level = save_file.split()[0]

        data['score'] = save_file.split()[1]

    except:

        saved_level = 10

    data = load_level(data, saved_level)

    return data

        
def load_level(data, level):

    ##  All data related to difficulty is derived from level value.

    ##  Subsequence (sub-fsm) for playing animation sequence.

    if data['play_animation'] == 0:

        ##  Block higher level state changes to allow animation to play.

        data['play_animation'] = 10
        data['prev_timer_delay'] = data['timerDelay']
        data['timerDelay'] = 60

        ##  Only edit level data at beginning of level-up animation
        ##  Derive difficulty of game solely from level.

        new_max_random = level + 2

        data['level'] = level
        data['max_random'] = new_max_random
        data['target_n'] = random.randrange(1, new_max_random)
        data['timerDelay'] = data['timer_delay_init'] - level * 10 
    
    elif data['play_animation'] > 0:

        data['play_animation'] -= 1
    
    if data['play_animation'] == 0:

        data['next_state'] = 'play'
        
        data['timerDelay'] = data['prev_timer_delay']

    return data
