from create_midi_file import *
from scale import *

for i in range(10):
    midifile = Midifile(172, 'random', f_maj, 80, 'test' + str(i))
    i += 1
