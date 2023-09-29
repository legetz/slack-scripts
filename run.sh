#!/bin/bash
set -eo pipefail

echo "Running script $1"
python src/$1.py