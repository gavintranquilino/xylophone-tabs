import mido

input_file = 'C:\\Users\\Gavin\\Downloads\\PlayedOnKeybaord.MID'
output_file = 'output.txt'

def midi_events(midi_file, output_file):
    try:
        mid = mido.MidiFile(midi_file)
        events = []
        for track in mid.tracks:
            for message in track:
                # message types: note_on, note_off, control_change, end_of_track 
                if message.type in ['note_on', 'note_off', 'control_change']:
                    events.append(str(message))
        
        return '\n'.join(events)
        
    except FileNotFoundError:
        print('MIDI file not found!')

def save_midi_events(midi_events):
    with open(output_file, 'w') as file:
        file.write(midi_events)

    return

def midi_data(midi_file, output_file):
    mid = mido.MidiFile(midi_file)
    for i, track in enumerate(mid.tracks):
        print('Track {}: {}'.format(i, track.name))
        for msg in track:
            print(msg)


if __name__ == "__main__":
    save_midi_events(midi_events(input_file, output_file))
    
    # Print all parsed midi data just out to console
    # midi_data(input_file, output_file)