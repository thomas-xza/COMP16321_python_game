#!/usr/bin/env python3

##  The template of this code is from Carnegie Mellon:
##    https://www.cs.cmu.edu/~112-n19/notes/notes-animations-part2.html
##    Because I didn't want to spend days building this concept!

##  Comments added to figure out how it works, various redundant parts
##    deleted.

from tkinter import *
import random


##  Initialise some values.
    
def init(data):

    ##  timerDelay is speed of frame changes.
    ##  100 millisecond == 0.1 seconds
    
    data.timerDelay = 400
    data.level = 1
    data.hit_target = False
    data.max_random = 5
    data.target_n = random.randrange(0,data.max_random)

    
##  timerFired() is called at regular intervals.

def timerFired(data):

    data.random_n = random.randrange(0, data.max_random)

    if data.hit_target == True:

        data.hit_target = False
        data.level += 1
        data.timerDelay -= 50
        data.max_random += 1
        data.target_n = random.randrange(0,data.max_random)

    
def mousePressed(event, data):

    pass




def keyPressed(event, data):

    print(event)

    if data.target_n == data.random_n:
        data.hit_target = True
        

def redrawAll(canvas, data):

    canvas.create_text(data.width/2, data.height/3,
                       text=f"Hit keyboard at {data.target_n}!!",
                       font = ('', '50', ''))
    
    canvas.create_text(data.width/2, data.height/2,
                       text=str(data.random_n),
                       font = ('', '50', ''))

    canvas.create_text(data.width/2, data.height/5*4,
                       text=f"Current level: {data.level}",
                       font = ('', '20', ''))
    

####   Allegedly the below need not be edited whatsoever.
    
def run(width=800, height=600):
    
    def redrawAllWrapper(canvas, data):

        ##  Wipe the canvas.
        
        canvas.delete(ALL)

        ##  Create a blank rectangle.
        
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)

        ##  Add more data to it.
        
        redrawAll(canvas, data)
        
        canvas.update()

        
    def mousePressedWrapper(event, canvas, data):
        
        ##  Handle input data.
        
        mousePressed(event, data)
        
        ##  Redraw using new data.
        
        redrawAllWrapper(canvas, data)

        
    def keyPressedWrapper(event, canvas, data):

        keyPressed(event, data)

        ##  Redraw using new data.
        
        redrawAllWrapper(canvas, data)

        
    def timerFiredWrapper(canvas, data):

        ##  Process data.
        
        timerFired(data)

        ##  Redraw using new data.
        
        redrawAllWrapper(canvas, data)
        
        ##  Pause, then recursively(?) call this function.
        
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)

        
    ##  Create an empty class type, and initialise an object of it.
        
    class Struct(object):
        pass

    data = Struct()

    
    ##  Start initialising the object with data.
    
    data.width = width
    data.height = height
    init(data)

    
    ##  Initialise TK parts, load Canvas type to to TK root frame.
    
    root = Tk()
    canvas = Canvas(master=root, width=data.width, height=data.height)
    canvas.pack()

    
    ##  Add key bindings to trigger functions based on user input.
    
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))

    
    ##  
    
    timerFiredWrapper(canvas, data)

    
    ##  Run event loop.
    
    root.mainloop()

run()
