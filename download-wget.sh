#!/bin/bash
set -eux

# --timestamping skips downloads
# if already downloaded the latest version.
# see also --no-clobber
wget \
    --show-progress \
    --timestamping \
    --directory-prefix=downloads/ \
    --input-file=urls.txt
