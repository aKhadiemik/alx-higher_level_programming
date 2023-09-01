#!/bin/bash
# Display accepted HTTP methods
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
