from mido import MidiTrack, MidiFile, Message


def create_note(note_height, note_delay, note_time):
    return Message("note_on", note=note_height, time=note_delay), Message("note_off", note=note_height, time=note_time)


def add_note_to_track(track: MidiTrack, note_height: list, note_delay: list, note_time: list, name: str = ""):
    track.name = name

    if len(note_height) == len(note_delay) and len(note_height) == len(note_time):
        for i in range(len(note_height)):
            track.append(create_note(note_height[i], note_delay[i], note_time[i])[0])
            track.append(create_note(note_height[i], note_delay[i], note_time[i])[1])
            print(find_note(note_height[i]))
    else:
        raise ValueError("Lengths of all 3 parameter list are not the same")
    return track


def find_note(note):
    note_list = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
    octave = 0
    while note > 11:
        note -= 12
        octave += 1
    note_name = note_list[note]
    return "octave:" + str(octave) + " note:" + str(note) + " (" + str(note_name) + ")"


# todo: changer la fonction create_note pour qu'elle prenne en paramettre le nom et l'octave des notes
# (et non pas le numéro de la hauteur)

if __name__ == "__main__":
    mid = MidiFile()
    piano_track = MidiTrack()
    mid.tracks.append(piano_track)

    list_note_height = [63, 65, 66, 68, 70, 75, 73, 70]
    list_note_delay = [0, 0, 0, 0, 0, 300, 0, 0]
    list_note_time = [300, 300, 300, 300, 300, 300, 300, 300]

    add_note_to_track(piano_track, list_note_height, list_note_delay, list_note_time)

    mid.save("new_song.mid")
