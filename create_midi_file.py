import random
from midiutil.MidiFile import MIDIFile
import scale_db
import pitches


def calc_duration(random_duration):
    if random_duration:
        duration = random.randint(1, 8)
    else:
        duration = 1
    return duration


class Midifile:
    time, track = 0, 0

    def __init__(self, bpm, random_duration, root_note, mode, max_range, length, track_name):
        mf = MIDIFile(1)
        mf.addTrackName(self.track, self.time, track_name)
        mf.addTempo(self.track, self.time, bpm)

        for i in range(length):
            if self.time <= length:
                duration = calc_duration(random_duration)
                note = scale_db.return_scale(root_note=root_note, mode=mode)[random.randint(0, 6)]
                pitch = pitches.convert_pitch(note_to_convert=note)
                velocity = random.randint(75, 100)
                pitch += (random.randint(1, max_range) * 12)
                if random.randint(1, 4) != 4:
                    mf.addNote(self.track, 0, pitch, self.time, duration, velocity)
                self.time += duration

        with open(f'output/{track_name}.mid', 'wb') as output_file:
            mf.writeFile(output_file)

        print(f'Created midi file: {track_name}.mid')




