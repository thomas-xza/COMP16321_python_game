#!/usr/bin/env python3

import random

    
def handle_state_initialisation(resolution, images):

    data = {}

    ##  Basic graphical data.

    data['width'] = resolution[0]
    data['height'] = resolution[1]

    ##  Images.
    
    data['frames'] = images[0]
    data['img_walk'] = images[1]
    data['img_walk_pos'] = 50
    data['img_stand'] = images[2]
    data['img_stand_pos'] = data['width'] - 50

    ##  Set initial state data of main FSM.

    data['state'] = 'play'
    data['next_state'] = 'play'

    data['level'] = 1
    data['level_up_src'] = ''
    
    data['max_random'] = 3
    data['target_n'] = random.randrange(1, data['max_random'])
    data['random_n'] = random.randrange(1, data['max_random'])

    data['score'] = 10
    data['play_animation'] = 0

    ##  Set initial state date of secondary mini FSM.

    data['character_state'] = 0
    
    ##  clock_time is speed of frame changes.
    ##  100 millisecond == 0.1 seconds
    
    data['clock_time_init'] = 400
    data['clock_time'] = data['clock_time_init']
    data['clock_time_prev'] = data['clock_time_init']

    ##  Highscore feature

    data['highscores'] = {}
    data['highscore_new_entry'] = ""
    
    ##  Extra features

    data['saved'] = False
    data['darkmode'] = True
    data['cheat_presses'] = 0

    return data
