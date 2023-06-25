#!/usr/bin/env python

import re
from pathlib import Path

import webvtt
from webvtt import Caption

DIRECTORY_LABELS = Path("labels/")


def filter_captions_by_speaker(speakers: list[str], captions: list[Caption]) -> dict[str, list[Caption]]:
    speakers_pipes = "|".join(speakers)
    speaker_label = re.compile(f"^({speakers_pipes}): ")

    caps_by_speaker = {sp: [] for sp in speakers}
    speaker = ""
    for cap in captions:
        match = speaker_label.match(cap.text)
        if match:
            speaker = match.group(1)

        if speaker:
            caps_by_speaker[speaker].append(cap)

    return caps_by_speaker


def captions_to_label_track(captions: list[Caption]) -> list[str]:
    # https://manual.audacityteam.org/man/importing_and_exporting_labels.html
    labels = []
    for cap in captions:
        lab = f"{cap.start_in_seconds}\t{cap.end_in_seconds}\n"
        labels.append(lab)
    return labels


def main():
    # test values
    sub_file = "subtitles/Where Do We Begin? Episode #1: The Future Of Podcasting.sbv"
    speakers = [
        "Baaulp",
        "Gir",
        "Log",
        "Trog",
        "Wayne",
    ]
    # load captions
    print(f"loading captions from {sub_file}")
    captions = webvtt.from_sbv(sub_file)
    print("loaded captions")

    # filter
    print(f"filtering captions with {len(speakers)} speakers")
    caps_by_speaker = filter_captions_by_speaker(speakers, captions)
    print("filtered captions")

    # write to label tracks
    DIRECTORY_LABELS.mkdir(exist_ok=True)
    for name, captions in caps_by_speaker.items():
        print(f"{name} // {len(captions)}")
        # get file to write to
        file_path = DIRECTORY_LABELS.joinpath(name).with_suffix(".txt")
        with open(file_path, "w") as file:
            # convert to label track
            label_lines = captions_to_label_track(captions)
            # write it
            file.writelines(label_lines)


if __name__ == '__main__':
    main()
