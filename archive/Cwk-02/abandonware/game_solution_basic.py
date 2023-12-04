#!/usr/bin/env python3

##  Admittedly I'd rather build it in JS, deploy on pages.dev

import tkinter as tk
import random

window = tk.Tk()

frame_a = tk.Frame()
frame_b = tk.Frame()
frame_c = tk.Frame()

max = 100

n_target = random.randrange(1,max)

intro = tk.Label(master=frame_a, text=f"Stop when the number is {n_target}")

intro.pack()

n = random.randrange(0,max)

play_status = tk.Label()


def play(n):

    play_status["text"] = f"{n}, fail!"

    
main_button = tk.Button(
    master=frame_b,
    relief=tk.FLAT,
    text=str(n),
    command=play(n)
    )

main_button.pack()

level_n = 1;

level_status = tk.Label(master=frame_c, text=f"Level: {level_n}")
level_status.pack()


frame_a.pack()
frame_b.pack()
frame_c.pack()


window.mainloop()
