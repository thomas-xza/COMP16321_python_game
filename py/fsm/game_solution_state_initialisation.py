#!/usr/bin/env python3

import random

    
def handle_state_initialisation(data):

    ##  Set initial state data.

    data['state'] = 'play'
    data['next_state'] = 'play'

    data['level'] = 1
    
    data['max_random'] = 3
    data['target_n'] = random.randrange(1, data['max_random'])
    data['random_n'] = random.randrange(1, data['max_random'])

    data['score'] = 10
    data['play_animation'] = 0

    
    ##  timerDelay is speed of frame changes.
    ##  100 millisecond == 0.1 seconds
    
    data['timer_delay_init'] = 400
    data['timerDelay'] = data['timer_delay_init']
    data['prev_timer_delay'] = data['timerDelay']


    ##  Highscore feature

    data['highscores'] = {}
    data['highscore_new_entry'] = ""

    
    ##  Extra features
    
    data['darkmode'] = True

