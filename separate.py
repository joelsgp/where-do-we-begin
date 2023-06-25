#!/usr/bin/env python

import re

import webvtt

sub_file = "subtitles/test.sbv"
speakers = [
    "Baaulp",
    "Gir",
    "Log",
    "Trog",
    "Wayne",
]

speakers_pipes = "|".join(speakers)
speaker_label = re.compile(f"^({speakers_pipes}): ")

caps = webvtt.from_sbv(sub_file)

# split captions by speaker
caps_by_speaker = {sp: [] for sp in speakers}
speaker = ""
for caption in caps:
    match = speaker_label.match(caption.text)
    if match:
        speaker = match.group(1)
    caps_by_speaker[speaker].append(caption)

print(caps_by_speaker)
