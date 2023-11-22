#!/usr/bin/env python3

##  The template of this is adapted MVC code from Carnegie Mellon:
##    https://www.cs.cmu.edu/~112-n19/notes/notes-animations-part2.html
##    Because I didn't want to spend days learning about Tkinter.
##    Many comments added to figure out how it works, a few redundant
##    parts deleted, main data structure adjusted.



from tkinter import *

from py.fsm.game_solution_state_definitions import *
from py.fsm.game_solution_state_initialisation import *
from py.fsm.game_solution_state_transitions import *
from py.fsm.game_solution_state_presentations import *


##  See docs/state_diagram.svg for info on how these states work.

def main(width=1280, height=720):
    
    ##  Initialise TK parts, load Canvas type to TK root frame.
    
    root = Tk()

    canvas = Canvas(master=root,
                    width=width,
                    height=height,
                    background='black')

    ##  Load canvas to main window.

    canvas.pack()
    
    
    ##  Initialise dict for game data, load animation and values to it.
    
    data = {}
    
    animation = [PhotoImage(file='./img/explosion_medium_transparent_green.gif',format = 'gif -index %i' %(i)) for i in range(10)]
    
    data = handle_state_initialisation([width, height], animation)


    ##  Add key binding which triggers callback upon user input.
    
    root.bind("<Key>", lambda event:
                            keyboard_trigger(event, canvas, data))


    ##  Add an initial event instance to the event loop.
    
    clock_trigger(canvas, data)

    
    ##  Run event loop.
    
    root.mainloop()


def draw_new_frame(canvas, data):

    ##  Wipe current canvas.

    canvas.delete(ALL)

    ##  Draw canvas.

    handle_state_presentation(canvas, data)


def keyboard_trigger(event, canvas, data):

    ##  Handle input data.

    handle_state_transitions(event.char, data)

    ##  Redraw using new data.

    draw_new_frame(canvas, data)


def clock_trigger(canvas, data):

    ##  Process data at fixed intervals.

    handle_state_definitions(data)

    ##  Redraw using new data.

    draw_new_frame(canvas, data)

    ##  Pause, then add another call to clock_trigger() to event loop,
    ##  to be triggered on the next clock tick, with game data as args.

    canvas.after(data['timerDelay'], clock_trigger, canvas, data)


if __name__ == "__main__":

    main()

