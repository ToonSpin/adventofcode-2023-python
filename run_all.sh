#!/bin/bash

divider='----------'
divider="${divider}${divider}"
divider="${divider}${divider}"
divider="${divider}${divider}"
for day in $(seq 24); do
    src_file=$(printf "src/day%02d.py" $day)
    data_file=$(printf "data/day%02d.txt" $day)
    if [ -e "${src_file}" ]; then
        caption=" DAY ${day}"
        echo "${divider:0:-${#caption}}${caption}"
        python3 "${src_file}" < "${data_file}"
    fi
done
