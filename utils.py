def get_midi_name_from_matched(h5_file, matched_scores):
    return max(matched_scores[h5_file].items(), key=lambda x: x[1])[0]