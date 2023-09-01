#!/bin/bash
# HTTP response displays size of body 
curl -s "$1" | wc -c
