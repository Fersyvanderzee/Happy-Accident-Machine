from create_midi_file import *
from scale import *


def test(bpm, scale, voices):
      for i in range(5):
        global midifile
        midifile = Midifile(bpm, 'random', scale, 80, 'test' + str(i+1), voices)
        i += 1


test(172, cmaj, 1)
