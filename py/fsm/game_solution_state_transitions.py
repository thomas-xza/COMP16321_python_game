#!/usr/bin/env python3

##  All state transitions occur as a result of keyboard inputs.

def handle_state_transitions(key, data):

    ##  All non-play states go back to state 'play' - see diagram.

    if data.state != 'play':

        data.next_state = play

    ##  State can change from 'play' depending on input.

    elif data.state == 'play':

        if key == 's':
        
            data.next_state = 'leaderboard'

        elif key == 'b':

            data.next_state = 'bossmode'

        elif key == 'p':
        
            data.next_state = 'pause'

        elif key == 'c':

            data.next_state = 'level_up'
            data.level_up_src = 'cheat'

        elif key == 'l':

            data.next_state = 'level_up'
            data.level_up_src = 'load'

        else:

            if data.target_n == data.random_n:
            
                data.next_state = 'level_up'
                data.level_up_src = 'win'

    ##  Customisations, not states.
            
    if key == 'd':

        data.darkmode = not data.darkmode


        
