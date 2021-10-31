from create_midi_file import *

tracks = input('How many tracks: ')
bpm_u = input("Bpm: ")
scale_u = input("Scale: ")
length_u = input("Length: ")

for i in range(int(tracks)):
    track_name_u = input("Track_name: ")
    create_midi_file(bpm=int(bpm_u), duration_input='random', scale=scale_u, length=int(length_u), track_name=track_name_u)