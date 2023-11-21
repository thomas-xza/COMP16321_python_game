#!/usr/bin/env python3

##  The template of this code is from Carnegie Mellon:
##    https://www.cs.cmu.edu/~112-n19/notes/notes-animations-part2.html
##    Because I didn't want to spend days learning about Tkinter.
##  Many comments added to figure out how it works, a few redundant
##    parts deleted.

##  I did enjoy the finite state machine aspect of it, though.


from tkinter import *

from py.fsm.game_solution_state_definitions import *
from py.fsm.game_solution_state_initialisation import *
from py.fsm.game_solution_state_transitions import *
from py.fsm.game_solution_state_presentations import *


##  Initialise some values.
    
def init(data):

    handle_state_initialisation(data)

    
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

    draw_astral(canvas, data)

    handle_state_presentation(canvas, data)

    
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

    canvas = Canvas(master=root,
                    width=data.width,
                    height=data.height,
                    background='black')

    data.frames = [PhotoImage(file='./img/explosion_medium_transparent.gif',format = 'gif -index %i' %(i)) for i in range(10)]

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
