#!/usr/bin/env bash
set -euo pipefail

DIR="detyper"
KEEP="kind_context_policy.py"

while true; do
    git checkout HEAD -- "$DIR" ":(exclude)$DIR/$KEEP"
    git clean -fd "$DIR" -e "$KEEP"
    sleep 1
done