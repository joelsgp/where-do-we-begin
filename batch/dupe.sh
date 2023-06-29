#!/bin/bash
set -eux

base='Base'
dest=~/'src/VirtualBox VMs/_shared/batch'

for name in 'Base' 'Baaulp' 'Gir' 'Log' 'Trog' 'Wayne'
do
    new="${dest}/${name}.bat"
    cp "${base}.bat" "${new}"
    sed -i "s/${base}.wma/${name}.wma/" "${new}"
done
# then copy them to the desktop
