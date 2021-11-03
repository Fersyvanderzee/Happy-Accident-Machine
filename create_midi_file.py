import random
from midiutil.MidiFile import MIDIFile


class Midifile:
    time = 0
    track = 0
    notes_list = []

    def __init__(self, bpm, duration_input, scale, length, track_name):
        mf = MIDIFile(1)

        mf.addTrackName(self.track, self.time, track_name)
        mf.addTempo(self.track, self.time, bpm)

        for i in range(length):
            if self.time <= length:
                rest_check = random.randint(1, 4)

                if duration_input == 'random':
                    duration = random.randint(1, 8) * 2
                else:
                    duration = 2

                velocity = random.randint(75, 100)

                if rest_check != 4:
                    note = scale.return_notes()[random.randint(0, 6)]
                    pitch = scale.convert_pitch(note)
                    mf.addNote(self.track, 0, pitch, self.time, duration, velocity)

                    self.notes_list.append(note)
                    self.time += duration
                else:
                    self.time += duration
                    continue

        with open('output/' + track_name + '.mid', 'wb') as output_file:
            mf.writeFile(output_file)

        print(f'Created midi file: {track_name}.mid')

    def return_notes(self):
        return self.notes_list






