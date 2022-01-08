# Happy Accident Machine (v0.0.4)

Note: this is in development and might not work properly.
This program randomizes notes and converts them to a midi-file that can we used in your favorite DAW (Ableton, FL Studio, Reaper, etc).


## How it works

The user provides information such as track name, track length, what scale/key to use and randomizes the notes (within given scale) 
and note length and converts that to a midi-file. The midi-file is placed in the folder called 'output'.

This midi-file can be imported in any DAW that supports midi. The fun thing is that because there is an equal chance for every note to appear
in the midi-file, the results might be unexpected. As a amateur musician my self I often find myself to use the same kind of patterns I'm used to.
Not due to lack of creativity, but by the way our brains are built. This program is unbiased to what is 'supposed to sound right' or how music works
in general. That makes this a creative companion to fuel your own creativity.


## How to use it
First of all (obviously) you need to have Python3 installed.
If you have Python3 installed you can use pip to install MIDIUtil (https://pypi.org/project/MIDIUtil/) in order to use this program (pip install midiutil).
Now you can run the main.py script out of an IDE like PyCharm. See the instructions in de main.py.


## Upcoming

* At the moment it's quite a hassle to use this program, since it is in early development. Also, you need to have Python and several libs
installed to have it work properly. It would be nice to have a standalone website that can be used by anyone. I guess it is time to 
implement the Django framework!
* More variety in scales. At the moment it only supports major and minor scales, but not more advanced scales.
* More functions to have even more unexpected results, like circle of fifths etc.
