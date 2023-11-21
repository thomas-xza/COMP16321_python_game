#!/usr/bin/env python3

import subprocess

from py.gfx.game_solution_graphics import *


def handle_state_presentation(canvas, data):

    draw_astral(canvas,data)

    if data.play_success == False and data.pause == 0 and data.bossmode == False:
    
        canvas.create_text(data.width/2, data.height/2,
                           text=str(data.random_n),
                           font = ('', '50', ''),
                       fill=darkmode_val(data, True))

    elif data.pause == 2:

        canvas.create_text(data.width/2, data.height/2,
                           text="PAUSED!",
                           font = ('', '50', ''),
                       fill=darkmode_val(data, True))

    elif data.bossmode == True:

        pass

    else:

        canvas.create_image(
            data.width/2,
            data.height,
            image=data.frames[10 - data.play_success],
            anchor=S)

        canvas.create_text(data.width/2, data.height/2,
                           text=f"w00t!",
                           font = ('', '80', ''),
                       fill=darkmode_val(data, True))

        if data.play_success == 9:

            subprocess.Popen(["aplay", "mechanical_explosion.wav"])

    if data.bossmode == False:

        canvas.create_text(data.width/2, data.height/3,
                           text=f"Hit keyboard at {data.target_n}!!",
                           font = ('', '50', ''),
                           fill=darkmode_val(data, True))

        canvas.create_text(data.width/2, data.height/5*4,
                           text=f"Level: {data.level}",
                           font = ('', '20', ''),
                           fill=darkmode_val(data, True))

