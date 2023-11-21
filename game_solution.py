#!/usr/bin/env python3

##  The template of this code is from Carnegie Mellon:
##    https://www.cs.cmu.edu/~112-n19/notes/notes-animations-part2.html
##    Because I didn't want to spend days learning about Tkinter.
##  Many comments added to figure out how it works, a few redundant
##    parts deleted.

##  I did enjoy the finite state machine aspect of it, though.


from tkinter import *
import random
import subprocess
import sys

from py.fsm.game_solution_state_definitions import *
from py.fsm.game_solution_state_initialisation import *
from py.fsm.game_solution_state_transitions import *
from py.fsm.game_solution_state_presentations import *

from py.gfx.game_solution_graphics import *


##  Initialise some values.
    
def init(data):

    handle_state_initialisation(data)


    
##  timerFired() is called at regular intervals.
##    Is used to update state of game.

##  See state_diagram.svg for info on how these states work

def timerFired(data):

    handle_state_definitions(data)

    if data.pause == 0:

        data.random_n = random.randrange(0, data.max_random)
        
    elif data.pause == 2:

        data.prev_timer_delay = data.timerDelay
        data.timerDelay = 2**32

    elif data.pause == 1:

        data.timerDelay = data.prev_timer_delay
        data.pause = 0

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

        
def mousePressed(event, data):

    pass


def keyPressed(event, data):

    key = event.char

    handle_state_transitions(key, data)


def redrawAll(canvas, data):

    draw_astral(canvas, data)

    handle_state_presentation(canvas, data)

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


def draw_astral(canvas, data):

    canvas.create_oval(15, 170, 25, 180, fill=darkmode_val(data, True))

    canvas.create_oval(145, 95, 155, 105, fill=darkmode_val(data, True))

    canvas.create_oval(395, 595, 405, 605, fill=darkmode_val(data, True))

    canvas.create_oval(795, 395, 805, 405, fill=darkmode_val(data, True))

    canvas.create_oval(1195, 345, 1205, 355, fill=darkmode_val(data, True))

    canvas.create_line(20, 175, 150, 100, activedash=True, fill=darkmode_val(data, True), dash=(5, 5), width=2)
        
    canvas.create_line(150, 100, 400, 600, activedash=True, fill=darkmode_val(data, True), dash=(5, 5), width=2)
        
    canvas.create_line(800, 400, 400, 600, activedash=True, fill=darkmode_val(data, True), dash=(5, 5), width=2)
        
    canvas.create_line(800, 400, 1200, 350, activedash=True, fill=darkmode_val(data, True), dash=(5, 5), width=2)
        

    
####   Allegedly the below need not be edited whatsoever.
    
def run(width=800, height=600):

    
    def redrawAllWrapper(canvas, data):

        ##  Wipe the canvas.
        
        canvas.delete(ALL)

        ##  Create a blank rectangle.
        
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill=darkmode_val(data, False), width=0)

        ##  Add more data to it.
        
        redrawAll(canvas, data)
        
        canvas.update()

                
    def mousePressedWrapper(event, canvas, data):
        
        ##  Handle input data.
        
        mousePressed(event, data)
        
        ##  Redraw using new data.
        
        redrawAllWrapper(canvas, data)

        
    def keyPressedWrapper(event, canvas, data):

        ##  Handle input data.

        keyPressed(event, data)

        ##  Redraw using new data.
        
        redrawAllWrapper(canvas, data)

        
    def timerFiredWrapper(canvas, data):

        ##  Process data at fixed intervals.
        
        timerFired(data)

        ##  Redraw using new data.
        
        redrawAllWrapper(canvas, data)
        
        ##  Pause, then add another call to this function to event loop.
        
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)


    ##  Create an empty class, and initiate an object of it.

    ##  This is a quirky CMU hack around Python's long syntax,
    ##    i.e. allows data.value rather than data['value']. But it
    ##    breaks functional programming ideals, such as immutability
    ##    of variables.

    class Struct(object):
        pass

    data = Struct()

    
    ##  Initialise data in the object.
        
    data.width = width
    data.height = height
    init(data)

    
    ##  Initialise TK parts, load Canvas type to TK root frame.
    
    root = Tk()

    explosion_gif = PhotoImage(file="explosion.gif", format="gif - 3")
    
    canvas = Canvas(master=root,
                    width=data.width,
                    height=data.height,
                    background='black')

    data.frames = [PhotoImage(file='explosion_medium_transparent.gif',format = 'gif -index %i' %(i)) for i in range(10)]

    canvas.pack()
    
    
    ##  Add key bindings to trigger functions based on user input.
    
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))


    ##  Add an initial event instance to the event loop.
    
    timerFiredWrapper(canvas, data)

    
    ##  Run event loop.
    
    root.mainloop()

run(width=1280, height=720)
#run()
