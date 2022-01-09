note_dict = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']

mode_dict = {
    'Major': [0, 2, 2, 1, 2, 2, 2, 1],
    'Natural minor': [0, 2, 1, 2, 2, 1, 2, 2],
    'Harmonic minor': [0, 2, 1, 2, 2, 1, 3, 1],
    'Melodic minor': [0, 2, 1, 2, 2, 2, 2, 1],
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

fifths_conversion_dict = {
    'A': 'C',
    'A#': 'C#',
    'B': 'D',
    'C': 'D#',
    'C#': 'E',
    'D': 'F',
    'D#': 'F#',
    'E': 'G',
    'F': 'G#',
    'F#': 'A',
    'G': 'A#',
    'G#': 'B'
}


def return_scale(root_note, mode):
    notes_in_scale = []
    count = note_dict.index(root_note)
    for interval in mode_dict[mode]:
        if (count + interval) >= len(note_dict):
            count = (count + interval) - len(note_dict)
        else:
            count += interval
        notes_in_scale.append(note_dict[count])
    return notes_in_scale


def convert_to_fifth(note):
    return fifths_conversion_dict[note]


def return_scale_in_fifths(scale):
    converted_scale = []
    for note in scale:
        converted_scale.append(convert_to_fifth(note))
    return converted_scale

