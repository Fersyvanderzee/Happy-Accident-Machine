from create_midi_file import *

testing = True

if not testing:
    tracks = input('How many tracks: ')
    bpm_u = input("Bpm: ")
    scale_u = input("Scale: ")
    length_u = input("Length: ")

    for i in range(int(tracks)):
        track_name_u = input("Track_name: ")
        create_midi_file(bpm=int(bpm_u), duration_input='random', scale=scale_u, length=int(length_u),
                         track_name=track_name_u)

else:
    midifile = create_midi_file(bpm=int(172), duration_input='random', scale='Dmaj', length=int(80),
                                track_name='one')
    midifile = create_midi_file(bpm=int(172), duration_input='random', scale='Dmaj', length=int(80),
                                track_name='two')
    midifile = create_midi_file(bpm=int(172), duration_input='random', scale='Dmaj', length=int(80),
                                track_name='three')
    midifile = create_midi_file(bpm=int(172), duration_input='random', scale='Dmaj', length=int(80),
                                track_name='four')