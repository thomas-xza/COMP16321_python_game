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

        draw_play_frame(canvas, data, centre, f_size)
    
    elif data['state'] == 'pause' or data['state'] == 'save':

        if data['saved'] == True:

            draw_text(canvas, data, centre, data['height']/2,
                            "SAVED!",
                            f_size)

        else:
        
            draw_text(canvas, data, centre, data['height']/2,
                            "PAUSED!",
                            f_size)
        
    elif data['state'] == 'bossmode':

        pass

    elif data['state'] == 'level_up' or data['state'] == 'play_animation':

        draw_levelup_frame(canvas, data, centre, f_size)

    elif data['state'] == 'highscores_input':

        draw_text(canvas, data, centre, data['height']/3,
                           "Input your initials!",
                           f_size)

        draw_text(canvas, data, centre, data['height']/2,
                  data['highscore_new_entry'],
                  f_size)

    elif data['state'] == 'highscores_display':

        draw_highscores_display_frame(canvas,data, centre, f_size)


def draw_play_frame(canvas, data, centre, f_size):

    # draw_text(canvas, data, centre, data['height']/6,
    #           f"Hit keyboard at {data['target_n']}!!",
    #           f_size)

    draw_text(canvas, data, centre, data['height']/6*2,
              f"Hit keyboard at {data['target_n']}!!",
              f_size)

    draw_text(canvas, data, centre, data['height']/6*3,
              str(data['random_n']),
              f_size)

    draw_text(canvas, data, centre, data['height']/6*4,
              f"Score: {data['score']}",
              f_size)

    draw_text(canvas, data, centre, data['height']/6*5,
              f"Level: {data['level']}",
              f_size)

                      
def draw_levelup_frame(canvas, data, centre, f_size):

    canvas.create_image(
        centre,
        data['height'],
        image=data['frames'][9 - data['play_animation']],
        anchor='s')

    draw_text(canvas, data, centre, data['height']/2,
              "",
              f_size)

    if data['play_animation'] == 9:

        subprocess.Popen(["aplay", "mechanical_explosion.wav"])
                      

def draw_highscores_display_frame(canvas, data, centre, f_size):

    draw_text(canvas, data, centre, data['height']/3,
                       "HIGH SCORES TOP 5",
                       f_size)

    focus = data['height']/2

    dict_as_tuple = data['highscores'].items()
    
    ##   sorted(..., key=lambda item: item[x])
    ##                ^ Selects the element (by position) to sort by.
    
    sorted_scores = sorted(dict_as_tuple, key=lambda item: item[1])

    sorted_scores.reverse()

    pos_y_append = 75

    for score in sorted_scores:

        draw_text(canvas, data, centre, data['height']/3 + pos_y_append,
                  f"{score[0]} {score[1]}",
                  f_size)

        pos_y_append += 75
        



    
