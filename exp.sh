#!/bin/bash
set -euo pipefail

source cinder_env/bin/activate
python3 run_all_proportion_benchmarks.py
