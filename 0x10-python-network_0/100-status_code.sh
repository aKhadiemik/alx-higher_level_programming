#!/bin/bash
# Send GET and display response status code for specified URL.
curl -s -o /dev/null -w "%{http_code}" "$1"
