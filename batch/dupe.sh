#!/bin/bash
set -eux

base='Base'
source='batch'
dest=~/'src/VirtualBox VMs/_shared/batch'

for name in 'Base' 'Baaulp' 'Gir' 'Log' 'Trog' 'Wayne'
do
    old="${source}/${base}.bat"
    new="${dest}/${name}.bat"
    cp "${old}" "${new}"
    sed -i "s/${base}.wma/${name}.wma/" "${new}"
done
# then copy them to the desktop
