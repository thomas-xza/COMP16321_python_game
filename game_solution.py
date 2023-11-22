#!/usr/bin/env python3

##  The concepts of this are adapted MVC code from Carnegie Mellon:
##    https://www.cs.cmu.edu/~112-n19/notes/notes-animations-part2.html
##    Because I didn't want to spend days learning about Tkinter.
##    Many comments added to figure out how it works, a few redundant
##    parts deleted, main data structure adjusted.


from tkinter import *

from py.fsm.definitions import *
from py.fsm.initialisation import *
from py.fsm.transitions import *
from py.fsm.presentations import *


##  See docs/state_diagram.svg for info on how these states work.

def main(width=1280, height=720):
    
    ##  Initialise TK parts, load Canvas type to TK root frame.
    
    main_window = Tk()

    canvas = Canvas(master=main_window,
                    width=width,
                    height=height,
                    background='black')

    ##  Load canvas to main window.

    canvas.pack()
    
    
    ##  Initialise dict for game data, load animation and values to it.
    
    data = {}
    
    animation = [PhotoImage(file='./img/explosion_medium_transparent_green.gif',format = 'gif -index %i' %(i)) for i in range(10)]
    
    man_walk = [PhotoImage(file='./img/walking_man_big.gif')]
    
    man_stand = [PhotoImage(file='./img/standing_man_big.gif')]

    images = [animation, man_walk, man_stand]
    
    data = handle_state_initialisation([width, height],images)


    ##  Add key binding which triggers callback to user_input_trigger()
    ##    at user input.
    
    main_window.bind("<Key>", lambda event:
                            user_input_trigger(event, canvas, data))


    ##  Add 1st clock trigger to the event loop.
    
    clock_trigger(canvas, data)

    
    ##  Run event loop.
    
    main_window.mainloop()


def user_input_trigger(event, canvas, data):

    print(event)

    ##  Take input data and change state.

    data = handle_state_transitions(event.char, data)


def clock_trigger(canvas, data):

    ##  Process inputs and current state data upon the clock tick.

    data = handle_state_definitions(data)

    ##  Wipe old frame.

    canvas.delete(ALL)

    ##  Draw new frame based on new data.

    handle_state_presentation(canvas, data)

    ##  Pause, then add another call to clock_trigger() to event loop,
    ##  to be triggered after delay (clock tick), with game data as args.

    canvas.after(data['clock_time'], clock_trigger, canvas, data)


if __name__ == "__main__":

    main()

