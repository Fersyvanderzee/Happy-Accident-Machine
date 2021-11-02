import random
from midiutil.MidiFile import MIDIFile
from scales import *


def create_midi_file(bpm, duration_input, scale, length, track_name):
    mf = MIDIFile(1)
    time = 0
    track = 0
    notes_list = []

    mf.addTrackName(track, time, track_name)
    mf.addTempo(track, time, bpm)

    for i in range(length):
        if time <= length:
            rest_check = random.randint(1,2)
            if rest_check == 4:
                note = 0
                pitch = 0
            else:
                note = allowed_pitches(scale)[random.randint(0, 6)]
                pitch = convert_to_pitch(note)

            if duration_input == 'random':
                duration = random.randint(1, 8) * 2
            else:
                duration = 2

            velocity = random.randint(75, 100)

            mf.addNote(track, 0, pitch, time, duration, velocity)

            notes_list.append(note)
            time += duration

    with open('output/' + track_name + '.mid', 'wb') as output_file:
        mf.writeFile(output_file)

    print(f'Created midi file: {track_name}.mid')

    return notes_list


def create_fifth_midi_file(bpm, duration_input, length, track_name, list_notes):
    mf = MIDIFile(1)
    time = 0
    track = 0
    notes_list = []

    mf.addTrackName(track, time, track_name)
    mf.addTempo(track, time, bpm)

    converted_list = calc_fifth(list_notes)

    for note in converted_list:
        pitch = convert_to_pitch(note)

        if duration_input == 'random':
            duration = random.randint(1, 8)
        else:
            duration = 1

        velocity = random.randint(75, 100)

        mf.addNote(track, 0, pitch, time, duration, velocity)

        notes_list.append(note)
        time += duration

    with open('output/' + track_name + '.mid', 'wb') as output_file:
        mf.writeFile(output_file)

    print(f'Created midi file: {track_name}.mid')

    return notes_list





