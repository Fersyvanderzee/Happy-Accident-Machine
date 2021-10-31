import random
from midiutil.MidiFile import MIDIFile
from scales import *

def create_midi_file(bpm, duration_input, scale, length, track_name):
    mf = MIDIFile(1)
    pitches = []
    time = 0
    track = 0


    mf.addTrackName(track, time, "Test1")
    mf.addTempo(track, time, bpm)

    for i in range(length):
        pitch = allowed_pitches(scale)[random.randint(0, 6)]
        if duration_input == 'random':
            duration = random.randint(1, 4)
        else:
            duration = 1

        mf.addNote(track, 0, pitch, time, duration, 100)
        time += duration
        pitches.append(pitch)
        print(str(pitch) + ' : ' + str(duration))

    with open('output/' + track_name + '.mid', 'wb') as output_file:
        mf.writeFile(output_file)
    print(pitches)


create_midi_file(bpm=120, duration_input='random', scale='Cmaj', length=40, track_name='test1')
create_midi_file(bpm=120, duration_input='random', scale='Cmaj', length=40, track_name='test2')