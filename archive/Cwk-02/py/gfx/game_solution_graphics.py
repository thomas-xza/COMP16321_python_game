#!/usr/bin/env python3


def initialise_canvas(canvas, data):

    ##  Create a blank new one.

    canvas.create_rectangle(0, 0, data['width'], data['height'],
                                fill=darkmode_val(data, False), width=0)

    ##  Draw a background
    
    draw_astral(canvas,data)


def darkmode_val(data, text):

    if text == True:

        if data['darkmode'] == True:

            return 'white'

        else:

            return 'black'

    if text == False:

        if data['darkmode'] == True:

            return 'black'

        else:

            return 'white'


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
        

def draw_text(canvas, data, pos_x, pos_y, text, f_size):

    canvas.create_text(pos_x, pos_y,
                       text=f"{text}",
                       font = ('', f_size, ''),
                       fill=darkmode_val(data, True))


