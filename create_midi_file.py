import random
from midiutil.MidiFile import MIDIFile
from scales import *


def create_midi_file(bpm, duration_input, scale, length, track_name):
    mf = MIDIFile(1)
    time = 0
    track = 0

    mf.addTrackName(track, time, track_name)
    mf.addTempo(track, time, bpm)

    for i in range(length):
        if time <= length:
            pitch = allowed_pitches(scale)[random.randint(0, 6)]
            if duration_input == 'random':
                duration = random.randint(1, 8)
            else:
                duration = 1

            mf.addNote(track, 0, pitch, time, duration, random.randint(60, 100))
            time += duration

    with open('output/' + track_name + '.mid', 'wb') as output_file:
        mf.writeFile(output_file)

    print(f'Created midi file: {track_name}.mid')