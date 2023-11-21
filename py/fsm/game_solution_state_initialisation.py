#!/usr/bin/env python3

import random

    
def handle_state_initialisation(data):

    ##  Set initial state.

    data.state = 'play'
    

    ##  timerDelay is speed of frame changes.
    ##  100 millisecond == 0.1 seconds
    
    data.timerDelay = 400
    data.prev_timer_delay = data.timerDelay


    ##  Level-up handling
    
    data.level = 1
    data.max_random = 1
    data.target_n = random.randrange(0,data.max_random)

    
    ##  Extra features
    
    data.darkmode = True

