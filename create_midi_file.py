import random
from midiutil.MidiFile import MIDIFile

from scale import return_closest_pitch


def rest_check():
    if random.randint(1, 4) != 4:
        return True
    else:
        return False


def calc_duration(input_duration):
    if input_duration == 'random':
        duration = random.randint(1, 8)
    else:
        duration = 2
    return duration






class Midifile:
    time = 0
    track = 0

    notes_list = []
    fifths_list = []

    def __init__(self, bpm, duration_input, scale, length, track_name, voices):
        mf = MIDIFile(1)

        mf.addTrackName(self.track, self.time, track_name)
        mf.addTempo(self.track, self.time, bpm)

        for i in range(length):
            if self.time <= length:

                duration = calc_duration(duration_input)
                if rest_check():
                    for voice in range(voices):
                        note = scale.return_notes()[random.randint(0, 6)]
                        pitch = scale.convert_pitch(note)
                        velocity = random.randint(75, 100)
                        self.notes_list.append(note)
                        if random.randint(1, 2) == 2:
                            pitch += 12
                        mf.addNote(self.track, 0, pitch, self.time, duration, velocity)
                        voice += 1

                    self.time += duration

                else:

                    self.notes_list.append('_')
                    self.fifths_list.append('_')
                    self.time += duration
                    continue

        with open('output/' + track_name + '.mid', 'wb') as output_file:
            mf.writeFile(output_file)

        print(f'Created midi file: {track_name}.mid')

    def return_notes(self):
        return self.notes_list

    def return_fifths(self):
        return self.fifths_list




