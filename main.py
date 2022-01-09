from kivy.app import App
from kivy.uix.widget import Widget

from create_midi_file import *


class HappyAccidentMachine(Widget):
    pass


class HappyAccidentMachineApp(App):
    root_note = ""
    mode = ""
    bpm = ""
    location = ""
    file_name = ""

    def build(self):
        return HappyAccidentMachine()

    def create_file(self):
        Midifile(bpm=172, random_duration=False, root_note=self.root_note,
                 mode=self.mode, max_range=1, length=80, track_name=self.file_name)
        print('File created!')

    # process inputs
    def process_root_note(self):
        self.root_note = str(self.root.ids.input.text)

    def process_mode(self):
        self.mode = str(self.root.ids.input.text)

    def process_bpm(self):
        print(type(self.root.ids.input.text))

    def process_location(self):
        self.location = str(self.root.ids.input.text)

    def process_file_name(self):
        self.file_name = str(self.root.ids.input.text)


if __name__ == "__main__":
    HappyAccidentMachineApp().run()
