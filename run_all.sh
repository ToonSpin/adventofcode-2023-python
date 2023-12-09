#!/bin/bash

for day in $(seq 24); do
    src_file=$(printf "src/day%02d.py" $day)
    if [ -e "${src_file}" ]; then
        caption="~DAY~${day}"
        printf "%80s\n" "${caption}" | tr ' ~' '- '
        python3 "${src_file}" < "$(printf "data/day%02d.txt" $day)"
    fi
done
