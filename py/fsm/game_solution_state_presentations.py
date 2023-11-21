#!/usr/bin/env python3

import subprocess

from py.gfx.game_solution_graphics import *


##  This function really should be broken out into:
##    draw_text(pos_x, pos_y, text, size, darkmode)

def handle_state_presentation(canvas, data):

    print("drawing...")

    draw_astral(canvas,data)

    f_size = 50

    centre = data['width']/2

    if data['state'] == 'play':
    
        draw_text(centre, data['height']/3,
                           "Hit keyboard at {data['target_n']}!!",
                           f_size)

        draw_text(centre, data['height']/3,
                           "Hit keyboard at {data['target_n']}!!",
                           f_size)

        draw_text(centre, data['height']/2,
                           str(data['random_n']),
                           f_size)

        draw_text(centre, data['height']/5*4,
                           f"Level: {data['level']}",
                           f_size)

    elif data['state'] == 'pause':

        draw_text(centre, data['height']/2,
                           "PAUSED!",
                           f_size)
        
    elif data['state'] == 'bossmode':

        pass

    elif data['state'] == 'level_up':

        canvas.create_image(
            centre,
            data['height'],
            image=data['frames'][9 - data['play_animation']],
            anchor='s')

        draw_text(centre, data['height']/2,
                  "w00t",
                  f_size)

        if data['play_animation'] == 9:

            subprocess.Popen(["aplay", "mechanical_explosion.wav"])

    elif data['state'] == 'highscores_input':

        draw_text(centre, data['height']/3,
                           "Input your initials!",
                           f_size)

        draw_text(centre, data['height']/2,
                  data['highscore_new_entry'],
                  f_size)

    elif data['state'] == 'highscores_display':

        draw_text(centre, data['height']/3,
                           "HIGH SCORES TOP 5",
                           f_size)

        focus = data['height']/2

        for k, v in data['highscores']:

            draw_text(centre, data
    
