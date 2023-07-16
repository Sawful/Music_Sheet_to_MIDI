from mido import MidiTrack, MidiFile, Message
# todo: doc string pour la classe et les fonctions
# output type
# clean


class NoteToMidi:
    def __init__(self, note_list: list = [], name: str = "new_song", file_path: str = "", show_note: bool = False):
        self.note_list = note_list
        self.name = name
        self.track = MidiTrack()
        self.show_note = show_note
        mid = MidiFile()
        mid.tracks.append(self.track)
        self.add_note_to_track()
        midi_file_path = name + ".mid" if file_path == "" else file_path + "/" + name + ".mid"
        mid.save(midi_file_path)

    @staticmethod
    def create_note(note_height : int = 0, note_delay: int = 0, note_time: int = 0):
        return Message("note_on", note=note_height, time=note_delay),\
            Message("note_off", note=note_height, time=note_time)

    def add_note_to_track(self):
        self.track.name = self.name

        # Verify that all values are the correct type
        for note in self.note_list:
            if not isinstance(note[0], str):
                raise ValueError(f"{note[0]} should be str")
            if not isinstance(note[1], int) or not isinstance(note[2], int) or not isinstance(note[3], int):
                raise ValueError(f"{note[1]}, {note[2]} and {note[3]},should all be int")

        for i in range(len(self.note_list)):
            height = self.find_height(self.note_list[i][0], self.note_list[i][1])
            self.track.append(self.create_note(height, self.note_list[i][2], self.note_list[i][3])[0])
            self.track.append(self.create_note(height, self.note_list[i][2], self.note_list[i][3])[1])

        if self.show_note:
            print(self._find_note())

        # return self.track

    @staticmethod
    def find_height(note : str = "C", octave : int = 0)-> int:
        note_list = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
        height = note_list.index(note) + 12 * octave
        return height

    def _find_note(self):
        for i in range (1, len(self.track)):
            if self.track[i].type != "note_off":
                height = self.track[i].note
                note_list = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
                octave = 0
                while height > 11:
                    height -= 12
                    octave += 1
                note_name = note_list[height]

                print ("octave:" + str(octave) + " height:" + str(height) + " (" + str(note_name) + ")")


if __name__ == "__main__":
    list_note = [["C", 5, 0, 300],
                 ["C#", 5, 0, 300],
                 ["D", 5, 0, 300],
                 ["D#", 5, 0, 300],
                 ["E", 5, 0, 300],
                 ["F", 5, 0, 300],
                 ["F#", 5, 0, 300],
                 ["G", 5, 0, 300],
                 ["G#", 5, 0, 300],
                 ["A", 5, 0, 300],
                 ["A#", 5, 0, 300],
                 ["B", 5, 0, 300]]

    NoteToMidi1 = NoteToMidi(list_note, file_path="Midi_files")
