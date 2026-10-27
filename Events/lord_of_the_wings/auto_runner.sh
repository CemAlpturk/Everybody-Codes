#!/bin/bash

if [ -z "$1" ]; then
  echo "Usage: ./auto_runner.sh <path_to_python_script>"
  exit 1
fi

SCRIPT_PATH="$1"

# Check if entr is installed
if ! command -v entr &> /dev/null; then
  echo "The 'entr' utility is not installed. Please install it (e.g., with 'brew install entr')"
  exit 1
fi

# Monitor and run the script on change
ls "$SCRIPT_PATH" | entr -c python "$SCRIPT_PATH"
