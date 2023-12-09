#!/bin/bash

for day in $(seq -w 24); do
    if [ -e "src/day${day}.py" ]; then
        echo "-------------------- DAY $day"
        python3 "src/day${day}.py" < "data/day${day}.txt"
    fi
done
