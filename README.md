
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
wrote a finite-state-machine on top of it. Initially I built with no
FSM, but it was a mess. Afterwards, I re-hashed the template around,
in a way that made more sense to me.

I originally discovered event loops in 2022, with Python's `asyncio`,
and then went on to more deeply understand them in 2023 with
Javascript's more native implementation.


##  Gameplay

The computer automatically cycles through a series of random numbers
within a range, you have to hit the keyboard when it reaches a certain
stated number. On success, there is an explosion and level-up. There
are some extra novelty features, to meet the specification.


##  Underlying Carnegie Mellon MVC template - how it works

The concepts from the CMU template are found within `game_solution.py`
*only*.

A diagram of their event loop is found here:
https://www.cs.cmu.edu/~112/notes/event_loop.png

A clock ticks at set intervals, the frequency of the ticks dependent
upon a numeric variable (implemented by a function that re-adds itself
to the event loop after a set period of time).

Further execution is then initiated by the following functions:

- A timer function is triggered every clock tick so calls further
  functions based on regular time invervals (like a sequential
  circuit)

- An user-input function is trigged by peripheral devices,
  e.g. keyboard (more like a combinatorial circuit)

Then a redrawing function takes the current data and makes graphical
actions based on it, using Tkinter's `canvas` type, which is called by
both the timer and the user-input functions.

There was a data structure issue with the CMU code - it used an object
which was an instance of an empty class, instead of a Python
dictionary, which makes debugging harder.


##  Overlaid finite state machine - how it works

See `docs/state_diagram.svg` for a diagram of the finite state machine.

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
`Coursework_02.pdf`) via the following means.

1. Images: explosion gif
2. Shapes: crummy astral background
3. Text: gameplay
4. Scoring: score is incremented/deincremented
5. Leaderboard: press `h` and input 3 characters
6. Resolution: 1280x720
7. Movement: text & animation timing
8. User can move object: n/a
9. Collision detection: n/a
10. Pause: press `p`
11. Customise: press `d` for darkmode
12. Cheat code: press `c` 10 times
13. Save load: press `s` or `l`
14. Boss key: press `b`

#8 and #9 are missing, but it may be possible to quickly hack in a few
characters that walk along the bottom and explode!


##  Resources

 - An intro to TKinter, and how the event loop works - https://realpython.com/python-gui-tkinter/#making-your-applications-interactive

- A template for running timers with Tkinter, from Carnegie Mellon University - https://www.cs.cmu.edu/~112-n19/notes/notes-animations-part2.html

- Pixel art explosion from Open Game Art - https://opengameart.org/content/animated-explosions

- Official Tkinter docs - https://tkdocs.com/shipman/intro.html

- What the VFX industry recommends to build GUIs -  https://vfxplatform.com/

- Feature creep - https://en.wikipedia.org/wiki/Feature_creep


##  Known bugs

Coming soon.


##  Final notes

I originally came around to software from Carnegie Mellon University
whilst setting up the HFSC algorithm on OpenWRT for a MIPS router in
an office with a limited uplink, after a tutor from a short course at
City University had taught me about a less dynamic, and therefore less
efficient, algorithm, to introduce quality-of-service networking
concepts. Sure enough, the HFSC algorithm worked exceptionally well,
and it put CMU on the radar for me in a big way.

If I ever need to build a desktop application, I will probably reach
for CMU's MVC, as it is quite productive relatively fast! Especially
for Python's standard library alone (e.g. compared to `asyncio` which
requires manually implementing the HTTP protocol to make asynchronous
HTTP requests, or `multiprocessing` which is a RAM hungry way to do
multicore).