#!/usr/bin/env python3

##  The template of this MVC code is from Carnegie Mellon:
##    https://www.cs.cmu.edu/~112-n19/notes/notes-animations-part2.html
##    Because I didn't want to spend days learning about Tkinter.
##  Many comments added to figure out how it works, a few redundant
##    parts deleted, main data structure adjusted.

##  I built a finite state machine on top of it.


from tkinter import *

from py.fsm.game_solution_state_definitions import *
from py.fsm.game_solution_state_initialisation import *
from py.fsm.game_solution_state_transitions import *
from py.fsm.game_solution_state_presentations import *


##  Initialise some values.
    
def init(data):


    
##  timerFired() is called at regular intervals.
##    Is used to update state of game.

##  See state_diagram.svg for info on how these states work.

def timerFired(data):

    handle_state_definitions(data)

        
def mousePressed(event, data):

    pass


def keyPressed(event, data):

    handle_state_transitions(event.char, data)


def redrawAll(canvas, data):

    handle_state_presentation(canvas, data)

    
####   Allegedly the below need not be edited whatsoever.
    
def run(width=800, height=600):

    
    def redrawAllWrapper(canvas, data):

        ##  Wipe the canvas.
        
        canvas.delete(ALL)

        ##  Create a blank rectangle object.
        
        canvas.create_rectangle(0, 0, data['width'], data['height'],
                                fill=darkmode_val(data, False), width=0)

        ##  Add data to it.
        
        redrawAll(canvas, data)

        ##  Load it.
        
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
        
        ##  Pause, then add another call to this function to event
        ##  loop, to be triggered on the positive clock edge.
        
        canvas.after(data['timerDelay'], timerFiredWrapper, canvas, data)


    ##  CMU's template was an object of an empty class.  However, this
    ##    is a bad hack, and was eventually changed...
    
    data = {}

    
    ##  Initialise data in the object.
        
    data = handle_state_initialisation([width, height])

    
    ##  Initialise TK parts, load Canvas type to TK root frame.
    
    root = Tk()

    canvas = Canvas(master=root,
                    width=data['width'],
                    height=data['height'],
                    background='black')

    data['frames'] = [PhotoImage(file='./img/explosion_medium_transparent_green.gif',format = 'gif -index %i' %(i)) for i in range(10)]

    # data['frames'] = [PhotoImage(file='./img/explosion.gif',format = 'gif -index %i' %(i)) for i in range(10)]

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
