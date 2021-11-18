from create_midi_file import *
from scale import *


def test(bpm, scale, voices, tracks):
    for i in range(tracks):
        Midifile(bpm, 'random', scale, 240, 'test' + str(i+1), voices)
        i += 1


# Generate the midi file!
# Use test(bpm, scale, voices)
# bpm = int
# scale = variable (so use cmaj instead of 'cmaj') See scale.py for all scales.
# voices = int

test(172, dmaj, 1, 10)
