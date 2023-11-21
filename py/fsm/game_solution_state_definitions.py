#!/usr/bin/env python3

import random


def handle_state_definitions(data):

    data.state = data.next_state
 
    if data.state == 'play':

        data.timerDelay = data.prev_timer_delay

    elif data.state == 'pause' or data.state == 'bossmode':

        data.prev_timer_delay = data.timerDelay
        data.timerDelay = 2**32

    elif data.state == 'leaderboard':

        pass

    elif data.state == 'level_up':

        data = handle_level_up_state(data)

        data.block_state_change = True

        data = handle_level_up(data)

        if data.level_up_src == 'cheat':

            data = load_level(data, 100)

        elif data.level_up_src == 'load':

            with open('savefile.txt', encoding="utf-8") as f:
                saved_level = int(f.read().strip())

            data = load_level(data, saved_level)

        elif data.level_up_src == 'win':

            data = load_level(data, data.level + 1)

    return data


def load_level(data, level):

    data.level = level

    data.max_random = level + 2

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
