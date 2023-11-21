
##  Foreword

Thought of this game whilst walking home one day. Haven't paid as much
attention to COMP16321 compared to other courses, so quickly put
something together, then realised it all needed rewriting properly.

The official TK website seemed to be extremely out of date, which was
off-putting, as I recently came out of a company still trapped in
Python 2 hell. "This is an unofficial mirror of Tkinter reference
documentation (based on Python 2.7 and Tk 8.5) created by the late
John Shipman.  It was last updated in 2013 and is unmaintained."

I didn't really want to learn *another* UI library, as I already had
to learn JS & React quickly this year, and indeed this whole game
could have been easily built with Javascript and React (and survived
online long-term, as a result).

Instead, I opted for a clock-based template for Tkinter, implemented
by Carnegie Mellon University, which fit nicely with COMP12111, then
wrote an FSM on top of it. Initially I built with no FSM, but it was a
mess.

I originally discovered event loops in 2022, with Python's `asyncio`,
and then went on to more deeply understand them in 2023 with
Javascript's more native implementation.


##  Gameplay

The computer automatically cycles through a series of random numbers
within a range, you have to hit the keyboard when it reaches a certain
stated number. On success, there is an explosion and level-up. There
are some extra novelty features, to meet the specification, but not
all of them - 'feature creep'!


##  Underlying Carnegie Mellon template - how it works

All CMU code is found within `game_solution.py` *only*.

A diagram of their event loop is found here:
https://www.cs.cmu.edu/~112/notes/event_loop.png

A clock ticks at set intervals, the frequency of the ticks dependent
upon a numeric variable.

Further execution is then initiated by the following functions:

- `timerFired()` is triggered every clock tick, and so calls functions
  based on regular time invervals (like a sequential circuit)

- `keyPressed()` and `mousePressed()` are triggered on user input
  (like a combinatorial circuit)

The function `redrawAll()` takes the current state and makes graphical
actions based on it, using Tkinter's `canvas` type, and is called
every clock tick or key input.

Heavy use of inline commenting has been made to make the template more
understandable. Furthering, the original template contained a poor
data structure - an object of an empty class, which makes debugging a
hassle. This was changed to a Python dictionary, for easier output.


##  Overlaid finite state machine by me - how it works

All code by me is found within `py/` directory *mainly* (also made a
few edits to `game_solution.py`).

See `state_diagram.svg` for a diagram of the finite state machine.

Some things to note about it:

- Pause and unpause do not increase or stop/start the clock, otherwise
  the game becomes unrecoverable, instead they hide the gameplay, and
  in this state the game only accepts input to unhide it

- Level up/load sequence temporarily changes the speed of the clock to
  a fixed rate, whilst playing an animation

- During gameplay, the speed of the clock (and other attributes
  related to the difficulty of the game) are derived via the level
  number


##  Other game details

A few sensory touches have been thrown in, such as using Python's
`subprocess` library to play sounds via Linux's `aplay`, upscaling
an animated pixel `.gif` and adjusting the `.gif` background to be
transparent.




##  Specification

The game meets the COMP16321 specifications (as mentioned in
Coursework_02.pdf) via the following means.

1. Images: explosion gif
2. Shapes: crummy astral background
3. Text: gameplay
4. Scoring: score is incremented/deincremented
5. Leaderboard: press 'l' and input 3 characters
6. Resolution: 1280x720
7. Movement: text & animation timing
8. User can move object: n/a
9. Collision detection: n/a
10. Pause: press `p`
11. Customise: press `d` for darkmode
12. Cheat code: press 'c' 10 times
13. Save load: press `s` or `l`
14. Boss key: press `b`


##  Resources

 - An intro to TKinter, and how the event loop works - https://realpython.com/python-gui-tkinter/#making-your-applications-interactive

- A template for running timers with Tkinter, from Carnegie Mellon University - https://www.cs.cmu.edu/~112-n19/notes/notes-animations-part2.html

- Pixel art explosion from Open Game Art - https://opengameart.org/content/animated-explosions

- Official Tkinter docs - https://tkdocs.com/shipman/intro.html

- What the VFX industry recommends to build GUIs -  https://vfxplatform.com/

- Feature creep - https://en.wikipedia.org/wiki/Feature_creep


##  Known bugs



##  Extra notes

I originally came around to Carnegie Mellon software whilst setting up
the HFSC algorithm on OpenWRT for a MIPS router in an office with a
limited uplink, after a tutor from a short course at City University
had taught me about a less dynamic, and therefore less efficient,
algorithm, to introduce quality-of-service networking concepts. Sure
enough, the HFSC algorithm worked exceptionally well, and it put CMU
on the radar for me in a big way.

