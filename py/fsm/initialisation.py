#!/usr/bin/env python3

import random

    
def handle_state_initialisation(resolution, animation):

    data = {}

    ##  Basic graphical data.

    data['width'] = resolution[0]
    data['height'] = resolution[1]
    data['frames'] = animation

    ##  Set initial state data.

    data['state'] = 'play'
    data['next_state'] = 'play'

    data['level'] = 1
    data['level_up_src'] = ''
    
    data['max_random'] = 3
    data['target_n'] = random.randrange(1, data['max_random'])
    data['random_n'] = random.randrange(1, data['max_random'])

    data['score'] = 10
    data['play_animation'] = 0
    
    ##  clock_time is speed of frame changes.
    ##  100 millisecond == 0.1 seconds
    
    data['clock_time_init'] = 400
    data['clock_time'] = data['clock_time_init']
    data['prev_clock_time'] = data['clock_time']

    ##  Highscore feature

    data['highscores'] = {}
    data['highscore_new_entry'] = ""
    
    ##  Extra features

    data['saved'] = False
    data['darkmode'] = True
    data['cheat_presses'] = 0

    return data
