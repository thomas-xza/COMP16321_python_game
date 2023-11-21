#!/usr/bin/env python3

import random

def handle_state_definitions(data):

    if data.state == 'pause':

        data.prev_timer_delay = data.timerDelay
        data.timerDelay = 2**32

    elif data.state == 'play':

        data.timerDelay = data.prev_timer_delay

    

    ##  Below is the level up & animation sequence.
        
    if data.hit_target == True:

        data.hit_target = False

        ##  Level up variables.
        
        data.level += 1
        data.max_random += 1
        data.target_n = random.randrange(0,data.max_random)

        ##  Play animation sequence

        data.play_success = 10
        data.prev_timer_delay = data.timerDelay
        data.timerDelay = 60

    if data.play_success > 0:

        data.play_success -= 1
    
    if data.play_success == 0:

        data.timerDelay = data.prev_timer_delay

    if data.cheatmode == 10:

        data.level += 100
        data.timerDelay = 20
        data.max_random = 2
        data.target_n = 1
        data.cheatmode = 0

    if data.save == True:

        with open('savefile.txt', encoding="utf-8") as f:
            f.write(data.level)

        data.save = False

    if data.load == True:

        with open('savefile.txt', encoding="utf-8") as f:
            data.level = int(f.read().strip())

        data.load = False
