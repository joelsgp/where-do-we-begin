# where do we begin
## files
- `download.py` - script for downloading podcast audio and cover images, then calling a script to merge them with ffmpeg.
- etc.

## usage
### scripts
Example use:
```shell
# create the file urls.txt
python download.py
# download the urls in urls.txt
./download-wget.sh
# merge audio and images into video
# this uses merge-test.sh which you can also run manually
python download.py
# at this point upload the video to youtube
# upload the transcript
# and download the resulting aligned subtitles
# create label tracks from subtitles
python separate.py
```

### audacity
working with the labelled audio
use Edit > Labelled Audio > Split Cut
https://manual.audacityteam.org/man/edit_menu_labeled_audio.html

for some reason I'm getting an error "There is not enough room available to paste the selection"
not trying to paste just trying to cut
https://manual.audacityteam.org/man/error_insufficient_space_in_track.html
"Split delete" works fine.

I could duplicate the main track for each speaker then split delte the inverse? seems impractical

ok it works if you do toggle Tracks > Sync-Lock Audio to ON
you might wanna mix down to mono to speed things up too
first mark out the first time each speaker talks, for offset. copy-paste the label track or whatever
1. select the source audio track and one of the label track
2. create a new stereo track and solo it
2. split cut from labelled audio
3. paste into a new track. make sure to select the point at which it starts, to get the right offset
4. immediately export, then clear the out-track, to avoid killing your pc
5. finally, export what remains of the original track


mix and render doesn't preserve start offset either

todo make a macro for this

ep. 1 is 01:42:39 and the intro is 24.019s

## links
### windows xp mode
- official
    - dead link http://www.microsoft.com/windows/virtual-pc/download.aspx
    - references it
- get wifi anywhere you go
    - https://download.cnet.com/Windows-XP-Mode/3000-18513_4-77683344.html
- archive.org
    - https://archive.org/details/windows-xp-mode_20200907
    - https://archive.org/download/windows-xp-mode_20200907/WindowsXPMode_en-us.zip
    - https://archive.org/download/windows-xp-mode_20200907/WindowsXPMode_en-us.zip/WindowsXPMode_en-us.exe
### ISO
- archive.org
    - https://archive.org/details/WinXPProSP3x86
    - https://archive.org/download/WinXPProSP3x86/en_windows_xp_professional_with_service_pack_3_x86_cd_vl_x14-73974.iso
    - the torrent is MUCH faster. lots of seeders
    - https://ia902601.us.archive.org/19/items/WinXPProSP3x86/WinXPProSP3x86_archive.torrent
### activation key
- https://gist.github.com/denizssch/72ec2aa1c5d0a84ffb57076f7dbf30d6
    - K6C2K-KY62K-DQR84-RD4QV-QB74Q
    - recommened by clowdcap, works
### virtualbox stuff
- https://www.virtualbox.org/wiki/Testbuilds
### windows media player
- https://wmpskinsarchive.neocities.org/


## notes
the basic display resolution for xp is 800x600
### visualisers
Ambient does NOT go fullscreen. this is not a driver issue or anything, it's just htat visualiser
OLDEST
- Ambience
- Plenoptic
- Battery
- Alchemy
NEWEST

1920/3 = 640
1080/2 = 540
640x540

gonna use guest size
1024x768

crop offset 192, 114

Base -- Bars
rest alphabetical, vote later
Baaulp - Alchemy
Gir -- Ambience
Log -- Battery
Trog -- Plenoptic
Wayne - Alchemy

mm not enough for each unique
all alchemy?

how to record multiple windows at once?
1. multiple vms - won't be able to sync them all
2. recording one-by-one - seems to be the main option
    - can do it unattended by putting them in a playlist
3. recording with virtualbox - kills performance
4. multiple obs instances - is this possible?
5. in-vm recorder - might be possible. have to find an old download
    - no OBS but these forum topics are funny https://obsproject.com/forum/threads/windows-xp-please-read.978/
    - https://www.reddit.com/r/windowsxp/comments/ps72dl/screen_recording_software/
    - http://web.archive.org/web/20221209193816/https://www.reddit.com/r/windowsxp/comments/ps72dl/screen_recording_software/
    - https://fraps.com/download.php
6. multiple vms, record all at once then sync in edit
7. see what Qemu offers
8. write a script to syncronise it
9. running them all in one vm - can't work, need fullscreen or crop. could fix it with editing too like 6.

do this tomorrow, don't have time to run it today.


### keyboard shortcuts
CTRL+P play
CTRL+S stp
CTRL+B back
CTRL+F Forwards
CTRL+SHIFT+B rewind
ALT+ENTER Fullscreen

Host+A adjust window size

next up: always-on livestream of all wdwb episodes with windows media player visualiser

was thinking of running it on the vm live, realised if I want to do the illuminati council thing I should pre-record it. for a single virtualiser I can run it live. take a poll what people like more?

no ui (api only)
1,000 free minutes per month (16 hours!)
https://symbl.ai/pricing/
https://docs.symbl.ai/docs/async-speaker-separation

no pretrained
https://github.com/facebookresearch/svoice
https://github.com/mindslab-ai/voicefilter
costs money
like £15 per hour of audio
https://www.simonsaysai.com/help/4176715-automatic-speaker-identification

### uploads
- podcast episode with visualisation
    https://youtu.be/740mzzQB0jQ
- demo of all visualisations
    https://youtu.be/ntyKbTLrfxE
    Description
    Music is 009 Sound System - Dreamscape https://youtu.be/TKfS5zVfGBc
    https://wmpvis.fandom.com/wiki/Alchemy
    https://wmpvis.fandom.com/wiki/Ambience
    https://wmpvis.fandom.com/wiki/Battery
    https://wmpvis.fandom.com/wiki/Plenoptic

try aligning transcription to subtitles with youtbe
https://wayneradiotv.fandom.com/wiki/Where_Do_We_Begin%3F_Episode_1:_The_Future_Of_Podcasting

channel I namecamped
https://www.twitch.tv/wheredowebegin

episodes
- https://wayneradiotv.podbean.com/
- episode 1 https://wayneradiotv.podbean.com/e/the-podcast-1-the-future-of-podcasting/
- episode 45 where they mentioned visualisations https://wayneradiotv.podbean.com/e/where-do-we-begin-episode-45-perfomance-enhancing-chanko/

NEED to record on obs with more bitrate. the fucking visualisers are huge bitrate eaters

todo
[ ] download all episodes. write a script to download them then attach the associated image to make video. may use lots of disk space
[ ] make transcripts into subtitles
[ ] run livesteam with visualiser
[ ] (maybe) figure out how to split speaker, make the illuminati real

AHAH:
0. I could search for something to segment audio by speaker. splitting crosstalk is not required.
2. REAL: I can use the transcripts! they're already captioned by name. I need to align the transcripts to timed text already anyway, for subtitles. eureeeek.

Title:
> 24/7 where do we begin podcast with visualiser. rtvs podcast (wayneradiotv, baaulp, trog, log, gir)
tags

I should ask rtvs by podcast email "if you were a wmp visualiser which one would you be" and ask permission to run the stream at the same time

could fork podcastparser to make it return a typed dict

I have to do all the podcast uploads to yt with still images before making visualisers, cause I need it to align the subs to split the tracks. UNLESS I can find a local tool to do it??
for splitting, I should get my program to just make an audacity label track. that simplifies things, then I do the hard part manually in audacity so I don’t have to fucking write it.
not free software https://www.captionhub.com/blog-post/automatically-align-transcript
“video transcript alignment”
only one github star, python2.7 + perl :/// https://github.com/polizoto/align_transcript
https://pypi.org/project/subaligner/
here we go https://github.com/baxtree/subaligner
https://github.com/amiaopensource/An_Archivists_Guide_To_Matroska/blob/master/metadata.md#adding-tags-with-ffmpeg

