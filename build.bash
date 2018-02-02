#!/bin/bash
outfile=${1:-creatures.md}
python rollcall.py > "$outfile"
