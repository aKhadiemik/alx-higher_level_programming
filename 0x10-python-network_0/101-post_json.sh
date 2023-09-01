#!/bin/bash
# Send JSON POST request to specified URL.
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
