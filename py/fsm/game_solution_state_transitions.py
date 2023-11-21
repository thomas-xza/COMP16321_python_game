#!/usr/bin/env python3

##  All state transitions occur as a result of keyboard inputs.

def handle_state_transitions(key, data):

    if data.state != 'play' and data.next_state == 'play':

        ##  All non-play states go back to state 'play' - see diagram.

        data.state = data.next_state

    elif data.state == 'pause' and key == 'p':

        data.next_state = 'play'

    elif data.state == 'play':

        ##  State can change from 'play' depending on input.

        if key == 'b':

            data.next_state = 'bossmode'

        elif key == 'p':
        
            data.next_state = 'pause'

        elif key == 's':
        
            data.next_state = 'leaderboard'

        elif key == 'c':

            data.next_state = 'level_up'
            data.level_up_src = 'cheat'

        elif key == 'l':

            data.next_state = 'level_up'
            data.level_up_src = 'load'

        else:

            ##  Catch any other key input.

            if data.target_n == data.random_n:
            
                data.next_state = 'level_up'
                data.level_up_src = 'win'

    ##  Customisations, not states.
            
    if key == 'd':

        data.darkmode = not data.darkmode
