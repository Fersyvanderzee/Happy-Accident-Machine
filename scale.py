import random


class Scale:
    notes = []
    fifth_notes = []

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
        bool_check = random.randint(1, 2)
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


def return_closest_pitch(pitches_to_allow, pitch):
    return min(pitches_to_allow, key=lambda x: abs(x - pitch))