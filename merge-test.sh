#!/bin/bash
set -eux

ffmpeg -i The_Podcast_1_-_The_Future_Of_Podcasting_Fixed_.mp3 -i Where_do_we_begin_ep1.jpg -tune stillimage -c:a copy test.mp4 -y
