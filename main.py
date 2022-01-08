from create_midi_file import *


def test(bpm, random_duration, root_note, mode, length, track_name, voices, tracks):
    for i in range(tracks):
        Midifile(bpm=bpm, random_duration=random_duration, root_note=root_note,
                 mode=mode, length=length, track_name=track_name + str(i), voices=voices)
        i += 1


test(bpm=172, random_duration=False, root_note='F#', mode='Harmonic minor', length=80, track_name='test', voices=1, tracks=1)
