class Scale:
    name = ''
    notes = []
    fifth_notes = []

    pitches = {  # pitches based on central C (C4).
        'C': 48,
        'C#': 49,
        'Db': 49,
        'D': 50,
        'D#': 51,
        'Eb': 51,
        'E': 52,
        'F': 53,
        'F#': 54,
        'Gb': 54,
        'G': 55,
        'G#': 56,
        'Ab': 56,
        'A': 57,
        'A#': 58,
        'Bb': 58,
        'B': 59
    }

    fifths = {
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

    def __init__(self, name, list_of_notes):
        self.notes = list_of_notes
        self.name = name

    def convert_pitch(self, note):
        pitch = self.pitches[note]
        return pitch

    def convert_fifth(self, note):
        fifth = self.fifths[note]
        return fifth

    def return_notes(self):
        return self.notes

    def return_name(self):
        return self.name

    def return_fifths(self):
        for note in self.notes:
            self.fifth_notes.append(self.fifths[note])
        return self.fifth_notes


cmaj = Scale('cmaj', ['C', 'D', 'E', 'F', 'G', 'A', 'B'])
dmaj = Scale('dmaj', ['C#', 'D', 'E', 'F#', 'G', 'A', 'B'])
emaj = Scale('emaj', ['C#', 'D#', 'E', 'F#', 'G#', 'A', 'B'])
fmaj = Scale('fmaj', ['C#', 'D#', 'E', 'F#', 'G#', 'A', 'Bb'])
gmaj = Scale('gmaj', ['C', 'D', 'E', 'F#', 'G', 'A', 'B'])
amaj = Scale('amaj', ['C#', 'D', 'E', 'F#', 'G#', 'A', 'B'])
bmaj = Scale('bmaj', ['C#', 'D#', 'E', 'F#', 'G#', 'A#', 'B'])
c_maj = Scale('c#maj', ['C', 'Db', 'Eb', 'F', 'Gb', 'Ab', 'Bb'])
d_maj = Scale('d#maj', ['C', 'D', 'Eb', 'F', 'G', 'Ab', 'Bb'])
f_maj = Scale('f#maj', ['C#', 'D#', 'F', 'F#', 'G#', 'A#', 'B'])
g_maj = Scale('g#maj', ['C', 'Db', 'Eb', 'F', 'G', 'Ab', 'Bb'])
a_maj = Scale('a#maj', ['C', 'D', 'Eb', 'F', 'G', 'A', 'Bb'])


def return_closest_pitch(pitches_to_allow, pitch):
    return min(pitches_to_allow, key=lambda x: abs(x - pitch))