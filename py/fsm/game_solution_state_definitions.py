#!/usr/bin/env python3

import random

def handle_state_definitions(data):

    data['state'] = data['next_state']
 
    state = data['state']

    print(data)
    
    if state == 'play':

        data['timerDelay'] = data['prev_timer_delay']
        data['random_n'] = random.randrange(1, data['max_random'])

    elif state == 'pause' or state == 'bossmode':

        data['prev_timer_delay'] = data['timerDelay']
        data['timerDelay'] = 2**32

    elif state == 'leaderboard':

        pass

    elif state == 'level_up':

        data = handle_level_up_state(data)

    return data


def handle_level_up_state(data):

    if data['level_up_src'] == 'cheat':

        data = load_level(data, 100)

    elif data['level_up_src'] == 'load':

        try:

            with open('savefile.txt', encoding="utf-8") as f:
                saved_level = int(f.read().strip())

        except:

            saved_level = 10

        data = load_level(data, saved_level)

    elif data['level_up_src'] == 'win':

        data = load_level(data, data['level'] + 1)

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

        new_max_random = level + 2

        data['level'] = level
        data['max_random'] = new_max_random
        data['target_n'] = random.randrange(1, new_max_random)
        data['timerDelay'] -= data['timerDelay'] // 20
    
    elif data['play_animation'] > 0:

        data['play_animation'] -= 1
    
    if data['play_animation'] == 0:

        data['next_state'] = 'play'
        
        data['timerDelay'] = data['prev_timer_delay']

    return data
