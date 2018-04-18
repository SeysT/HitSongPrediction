import midi, numpy


MAX_LENGTH = 2000


def midi_to_matrix(midifile, max_length=MAX_LENGTH):
    pattern = midi.read_midifile(midifile)
    pattern.make_ticks_abs()

    timeleft = max([track[-1].tick for track in pattern])
    pos = [0 for _ in pattern]
    time = 0

    channel_data = [[0, 0, 0] for _ in range(1, 17)]
    tempo = 0
    time_signature = [0, 0, 0, 0]

    statematrix = []

    if timeleft < max_length:
        import pdb; pdb.set_trace()

    while time <= timeleft and time < max_length:
        changed = True
        while changed:
            changed = False
            for track_number, track in enumerate(pattern):
                if pos[track_number] >= len(track):
                    continue

                event = track[pos[track_number]]
                if event.tick == time:
                    changed = True
                    if type(event) is midi.SetTempoEvent:
                        tempo = (event.data[0] << 16) + (event.data[1] << 8) + event.data[2]
                    elif type(event) is midi.TimeSignatureEvent:
                        time_signature = event.data
                    elif type(event) is midi.ProgramChangeEvent:
                        channel_data[event.channel][0] = event.data[0]
                    elif type(event) is midi.NoteOnEvent:
                        if event.data[1] == 0:
                            channel_data[event.channel][1] = 0
                            channel_data[event.channel][2] = 0
                        else:
                            channel_data[event.channel][1] = event.data[0]
                            channel_data[event.channel][2] = event.data[1]
                    elif type(event) is midi.NoteOffEvent:
                        channel_data[event.channel][1] = 0
                        channel_data[event.channel][2] = 0
                    else:
                        pass
                    pos[track_number] += 1

        state = time_signature + [tempo]
        for data in channel_data:
            state += data
        statematrix.append(numpy.array(state))

        time +=1
                
    return numpy.array(statematrix)


def get_midi_name_from_matched(h5_file, matched_scores):
    return max(matched_scores[h5_file].items(), key=lambda x: x[1])[0]


def data_generator(dirpath):
    while True:
        for file in os.listdir(dirpath):
            data = np.load(os.path.join(dirpath, file))
            X = np.array([x for x in data[0]])
            Y = data[1].astype(float)

            yield X, Y