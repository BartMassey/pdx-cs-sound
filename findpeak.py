#!/usr/bin/python3
# Copyright (c) 2019 Bart Massey
# [This program is licensed under the "MIT License"]
# Please see the file LICENSE in the source
# distribution of this software for license terms.

# Find maximum and minimum sample in an audio file.

import sys
import wave as wav

# Get the signal file.
wavfile = wav.open(sys.argv[1], 'rb')

# Channels per frame.
channels = wavfile.getnchannels()

# Bytes per sample.
width = wavfile.getsampwidth()

# Sample rate
rate = wavfile.getframerate()

# Number of frames.
frames = wavfile.getnframes()

# Length of a frame
frame_width = width * channels


# Get the signal and check it.
max_sample = None
min_sample = None
wave_bytes = wavfile.readframes(frames)
# Iterate over frames.
for f in range(0, len(wave_bytes), frame_width):
    frame = wave_bytes[f : f + frame_width]
    # Iterate over channels.
    for c in range(0, len(frame), width):
        # Build a sample.
        sample_bytes = frame[c : c + width]
        # XXX Eight-bit samples are unsigned
        sample = int.from_bytes(sample_bytes,
                                byteorder='little',
                                signed=(width>1))
        # Check extrema.
        if max_sample == None:
            max_sample = sample
        if min_sample == None:
            min_sample = sample
        if sample > max_sample:
            max_sample = sample
        if sample < min_sample:
            min_sample = sample

wavfile.close()

print("min: {}  max: {}".format(min_sample, max_sample))
