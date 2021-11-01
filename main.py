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
    midifile = create_midi_file(bpm=int(172), duration_input='random', scale='Cmaj', length=int(80),
                                track_name='test_regular')
    fifth_file = create_fifth_midi_file(bpm=int(172), duration_input='random', length=int(80),
                                        track_name='test_fifth', list_notes=midifile)
    print(midifile)
    print(fifth_file)
