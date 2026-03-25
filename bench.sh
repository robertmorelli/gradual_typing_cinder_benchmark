#!/bin/bash

avg() {
    local file=$1
    local total=0
    for i in $(seq 1 10); do
        t=$(python static-python-perf/Benchmark/nbody/advanced/$file 2>/dev/null)
        total=$(echo "$total + $t" | bc)
    done
    echo "$file: $(echo "scale=4; $total / 10" | bc)"
}

avg main.py
avg main.1.py