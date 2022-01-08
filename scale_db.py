note_dict = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#',
             'A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']

mode_dict = {
    'Major': [0, 2, 2, 1, 2, 2, 2, 1],
    'Natural minor': [0, 2, 1, 2, 2, 1, 2, 2],
    'Harmonic minor': [0, 2, 1, 2, 2, 1, 3, 1],
    'Melodic minor': [0, 2, 1, 2, 2, 2, 2, 2],
    'Dorian mode': [0, 2, 1, 2, 2, 2, 1, 2],
    'Phrygian mode': [0, 1, 2, 2, 2, 1, 2, 2],
    'Lydian mode': [0, 2, 2, 2, 1, 2, 2, 1],
    'Mixolydian mode': [0, 2, 2, 1, 2, 2, 1, 2],
    'Locrian mode': [0, 1, 2, 2, 1, 2, 2, 2],
    'Ahava raba mode': [0, 1, 3, 1, 2, 1, 2, 2],
    'Minor pentatonic': [0, 3, 2, 2, 3, 2],
    'Pentatonic': [0, 2, 2, 3, 2, 3],
    'Blues': [0, 3, 2, 1, 1, 3]
}


def return_scale(root_note, mode):
    notes_in_scale = []
    count = note_dict.index(root_note)
    for p in mode_dict[mode]:
        count += p
        notes_in_scale.append(note_dict[count])
    return notes_in_scale
