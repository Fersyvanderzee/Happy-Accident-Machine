import random
from midiutil.MidiFile import MIDIFile
import scale_db
import pitches


def rest_check():
    if random.randint(1, 4) != 4:
        return True
    else:
        return False


def calc_duration(random_duration):
    if random_duration:
        duration = random.randint(1, 8)
    else:
        duration = 2
    return duration


class Midifile:
    time, track = 0, 0

    notes_list = []
    fifths_list = []

    def __init__(self, bpm, random_duration, root_note, mode, length, track_name, voices):
        mf = MIDIFile(1)

        mf.addTrackName(self.track, self.time, track_name)
        mf.addTempo(self.track, self.time, bpm)

        for i in range(length):
            if self.time <= length:

                duration = calc_duration(random_duration)

                if rest_check():

                    for voice in range(voices):

                        note = scale_db.return_scale(root_note=root_note, mode=mode)[random.randint(0, 6)]

                        pitch = pitches.convert_pitch(note=note)

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




