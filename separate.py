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

    if speaker:
        caps_by_speaker[speaker].append(caption)


def captions_to_label_track(captions: list[webvtt.Caption]) -> list[str]:
    # https://manual.audacityteam.org/man/importing_and_exporting_labels.html
    labels = []
    for cap in captions:
        lab = f"{cap.start_in_seconds} → {cap.end_in_seconds} → \n"
        labels.append(lab)
    return labels


for name, captions in caps_by_speaker.items():
    with open(f"labels/{name}.txt", "w") as file:
        label_lines = captions_to_label_track(captions)
        file.writelines(label_lines)
