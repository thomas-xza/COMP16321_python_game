#!/usr/bin/env python3

##  All state transitions occur as a result of keyboard inputs.

def handle_state_transitions(key, data):

    if data['state'] != 'play' and data['next_state'] == 'play':

        data['state'] = data['next_state']

    elif data['state'] == 'pause' and (key == 'p' or key == 's'):

        data['next_state'] = 'unpause'

    elif data['state'] == 'bossmode' and key == 'b':

        data['next_state'] = 'play'

    elif data['state'] == 'highscores_input' and key.isalpha():

        data['highscore_new_entry'] += key

    elif data['state'] == 'highscores_display':

        data['next_state'] = 'play'

    elif data['state'] == 'play':

        ##  State can change from 'play' depending on input.

        # if key == 'a':

        ##  Ideally key would be right-arrow, but required refactoring.

        if key == 'a':

            data['character_state'] += 5

        if key == 'b':

            data['next_state'] = 'bossmode'

        elif key == 'h':
        
            data['next_state'] = 'highscores_input'

        elif key == 'p':
        
            data['next_state'] = 'pause'

        elif key == 's':
        
            data['next_state'] = 'save'

        elif key == 'c':

            data['next_state'] = 'level_up'
            data['level_up_src'] = 'cheat'

        elif key == 'l':

            data['next_state'] = 'level_up'
            data['level_up_src'] = 'load'

        else:

            ##  Catch any other key input.

            if data['target_n'] == data['random_n']:
            
                data['next_state'] = 'level_up'
                data['level_up_src'] = 'win'

    ##  Customisations, not states.
            
    if key == 'd':

        data['darkmode'] = not data['darkmode']

    return data

