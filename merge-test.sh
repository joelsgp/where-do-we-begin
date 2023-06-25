#!/bin/bash
set -eux

mp3_file="$1"
jpg_file="$2"
out_file="$3"
shift 3


ffmpeg \
    -i "${mp3_file}" \
    -framerate 1/10 -loop 1 -i "${jpg_file}" \
    -tune stillimage -c:a copy -shortest \
    "${@}" \
    "${out_file}" \
    -y
