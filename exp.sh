#!/bin/bash
set -euo pipefail

source cinder_env/bin/activate
python run_all_proportion_benchmarks.py
