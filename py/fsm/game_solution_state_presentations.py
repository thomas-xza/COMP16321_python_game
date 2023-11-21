#!/usr/bin/env python3

import subprocess

from py.gfx.game_solution_graphics import *


def handle_state_presentation(canvas, data):

    draw_astral(canvas,data)

    if data.state == 'play':
    
        canvas.create_text(data.width/2, data.height/3,
                           text=f"Hit keyboard at {data.target_n}!!",
                           font = ('', '50', ''),
                           fill=darkmode_val(data, True))

        canvas.create_text(data.width/2, data.height/2,
                           text=str(data.random_n),
                           font = ('', '50', ''),
                       fill=darkmode_val(data, True))

        canvas.create_text(data.width/2, data.height/5*4,
                           text=f"Level: {data.level}",
                           font = ('', '20', ''),
                           fill=darkmode_val(data, True))

    elif data.state == 'pause':

        canvas.create_text(data.width/2, data.height/2,
                           text="PAUSED!",
                           font = ('', '50', ''),
                       fill=darkmode_val(data, True))        

    elif data.state == 'bossmode':

        pass

    elif data.state == 'level_up':

        canvas.create_image(
            data.width/2,
            data.height,
            image=data.frames[10 - data.play_success],
            anchor=S)

        canvas.create_text(data.width/2, data.height/2,
                           text=f"w00t!",
                           font = ('', '80', ''),
                       fill=darkmode_val(data, True))

        if data.play_animation == 9:

            subprocess.Popen(["aplay", "mechanical_explosion.wav"])

