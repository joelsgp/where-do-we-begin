#!/bin/bash
set -eux

wget \
    --show-progress \
    --directory-prefix=downloads/ \
    --input-file=urls.txt
