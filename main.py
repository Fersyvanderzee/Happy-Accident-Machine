from create_midi_file import *


def create_file(bpm, random_duration, root_note, mode, length, track_name, voices, tracks):
    for i in range(tracks):
        Midifile(bpm=bpm, random_duration=random_duration, root_note=root_note,
                 mode=mode, length=length, track_name=track_name + str(i), voices=voices)
        i += 1


create_file(bpm=100, random_duration=False, root_note='D', mode='Harmonic minor',
            length=80, track_name='test', voices=1, tracks=3)


