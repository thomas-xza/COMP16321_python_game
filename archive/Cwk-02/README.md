
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

I found some template for a timer app for Tkinter, implemented by
Carnegie Mellon University, clock-based, which fit nicely with
COMP12111, then wrote a finite-state-machine on top of it. Initially I
built with no FSM, but it was a mess. Afterwards, I re-hashed the
template around, in a way that made more sense to me, however, the
logic of the MVC is so sound, that if I were to start from scratch,
I'd just be writing out something very similar.

I originally discovered event loops in 2022, with Python's `asyncio`,
and then went on to more deeply understand them in 2023 with
Javascript's more native implementation.


##  Gameplay

The computer automatically cycles through a series of random numbers
within a range, you have to hit the keyboard when it reaches a certain
stated number. On success, there is an explosion and level-up. There
are some extra novelty features, to meet the specification.

A secondary way to level-up is to move the character at the bottom of
the screen rightwards, until he collides with a twin-like character.


##  Underlying Carnegie Mellon MVC concepts - how they work

The concepts from the CMU template are found within `game_solution.py`
*only*.

A diagram of their event loop is found here:
https://www.cs.cmu.edu/~112/notes/event_loop.png

Ongoing execution is initiated by the following functions:

- A timer function is triggered every clock tick so calls further
  functions based on regular time invervals (like a sequential
  circuit), which then adds another instance of itself to the event
  loop before exiting

- A user-input function is trigged by peripheral devices,
  e.g. keyboard (more like a combinatorial circuit)

Then a redrawing function, which in the template is triggered both on
clock ticks and user-input, takes the current data and makes graphical
actions based on it, using Tkinter's `canvas` type (a large grid),
which is called by both the timer and the user-input functions.

There was a data structure issue with the CMU code - it used an object
which was an instance of an empty class, instead of a Python
dictionary, which makes debugging harder.

The concepts I have used are similar to the CMU template, except that
I have built something less monolithic to 1 file, which only updates
on the clock, and with a more sane data structure.

##  Overlaid finite state machines - how they work

See `docs/state_diagram.svg` for a diagram of the finite state machine.

There is 1 main finite state machine, state changes being queue in
`transitions.py` by keyboard input, and being further traversed by
clock ticks in `definitions.py`, which takes actions on different
states. `presentations.py` is oriented around the presentation of
different states.

Some things to note about it:

- Pause and unpause do not increase or stop/start the clock, otherwise
  the game becomes unrecoverable, instead they hide the gameplay, and
  in this state the game only accepts input to unhide it

- Level up/load sequence temporarily changes the speed of the clock to
  a fixed rate, whilst playing an animation

- During gameplay, the speed of the clock (and other attributes
  related to the difficulty of the game) are derived via the level
  number

There is a secondary finite machine, providing another method or
levelling up, which technically exists within the `play` state to
change the main FSM, but is graphically depicted as if somewhat
separate, as the graphics for it are more static.


##  Other game details

A few sensory touches have been thrown in, such as using Python's
`subprocess` library to play sounds via Linux's `aplay`, upscaling
an animated pixel `.gif` and adjusting the `.gif` background to be
transparent.


##  Specification

The game attemps to meet the COMP16321 specifications (as mentioned in
`Coursework_02.pdf`) via the following means.

1. Images: explosion gif
2. Shapes: basic astral background
3. Text: gameplay
4. Scoring: score is incremented/deincremented by gameplay
5. Leaderboard: press `h` and input 3 characters, stored to `highscores.json`
6. Resolution: 1280x720 fixed
7. Movement: move character across screen
8. User can move object: n/a
9. Collision detection: collide characters
10. Pause: press `p`
11. Customise: press `d` for darkmode
12. Cheat code: press `c` 10 times
13. Save load: press `s` or `l` to save/load to `savefile.txt`
14. Boss key: press `b`


##  Resources

 - An intro to TKinter, and how the event loop works - https://realpython.com/python-gui-tkinter/#making-your-applications-interactive

- A template for running timers with Tkinter, from Carnegie Mellon University - https://www.cs.cmu.edu/~112-n19/notes/notes-animations-part2.html

- Pixel art explosion from Open Game Art - https://opengameart.org/content/animated-explosions

- Pixel art little man from Open Game Art - https://opengameart.org/content/4-direction-isometric-human-male-standing-walk-attack

- Official Tkinter docs - https://tkdocs.com/shipman/intro.html

- What the VFX industry recommends to build GUIs -  https://vfxplatform.com/

- Feature creep - https://en.wikipedia.org/wiki/Feature_creep


##  Known bugs

After loading highscores, the speed goes into overdrive.


##  Final notes

I originally came around to software from Carnegie Mellon University
whilst setting up the HFSC algorithm on OpenWRT for a MIPS router in
an office with a limited uplink, after a tutor from a short course at
City University had taught me about a less dynamic, and therefore less
efficient, algorithm, to introduce quality-of-service networking
concepts. Sure enough, the HFSC algorithm worked exceptionally well,
and it put CMU on the radar for me in a big way.

If I ever need to build a desktop application, I will probably reach
for CMU's MVC, as it prototypes to productivity relatively fast,
especially for Python's standard library alone (e.g. compared to
`asyncio` which requires manually implementing the HTTP protocol to
make asynchronous HTTP requests, or `multiprocessing` which is a RAM
hungry way to do multicore), though the template does need essential
adjustments.