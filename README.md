
##  Foreword

Thought of this game whilst walking home one day. Haven't paid as much
attention to COMP16321 compared to other courses, so am quickly
putting something together. I didn't really want to learn *another* UI
library, as I already had to learn React quickly this year, and indeed
this whole game could have been built with Javascript and React (and
survived online long-term, as a result).

The official TK website seemed to be extremely out of date, which was
off-putting, as I recently came out of a company still trapped in
Python 2 hell. "This is an unofficial mirror of Tkinter reference
documentation (based on Python 2.7 and Tk 8.5) created by the late
John Shipman.  It was last updated in 2013 and is unmaintained."


##  Gameplay

The computer automatically cycles through a series of random numbers
within a range, you have to hit the keyboard when it reaches a certain
stated number. On success, there is an explosion and level-up. There
are some extra novelty features, to meet the specification, but not
all of them.


##  How it works

A timer runs at set intervals, which increases in speed based on the
current difficulty level, or is set to a fixed speed when trasition
animations are playing.

The logic regarding the states of the gameplay are handled by 1
function named timerFired(), and major changes to the state are
initially triggered by keyPressed() and mousePressed(). The function
redrawAll() takes the current state and makes graphical actions based
on it.

Note that there are some quirks inside the CMU template, such as using
an object of an empty class to store all state data, which seems to be
a workaround for shorter syntax than using a Python dictionary.



##  Specification

The game meets the COMP16321 specifications (as mentioned in
Coursework_02.pdf) via the following means.

1. Images: explosion gif
2. Shapes: astral background
3. Text: gameplay
4. Scoring: ___
5. Leadboard: ___
6. Resolution: 1280x720
7. Movement: text & animation timing
8. Move object: n/a
9. Collision detection: n/a
10. Pause: press 'p'
11. Customise: darkmode press 'd'
12. Cheat code: press 'c' 10 times
13. Save load: ___
14. Boss key: press 'b'


##  Resources

 - An intro to TKinter - https://realpython.com/python-gui-tkinter/#displaying-clickable-buttons-with-button-widgets

- A template for running timers from Carnegie Mellon University - https://www.cs.cmu.edu/~112-n19/notes/notes-animations-part2.html

- Pixel art explosion from Open Game Art - https://opengameart.org/content/animated-explosions


##  Extra notes

I originally came around to Carnegie Mellon software whilst setting up
the HFSC algorithm on OpenWRT for a router in an office with a limited
uplink, after a tutor from a short course at City University had
taught me about a less dynamic, and therefore less efficient,
algorithm, to introduce quality-of-service networking concepts. Sure
enough, the HFSC algorithm worked exceptionally well, and it put CMU
on the radar for me in a big way.