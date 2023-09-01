#!/bin/bash
# Send PUT request to catch_me hosted at localhost port 5000
curl -sL -X PUT -H "Origin: HolbertonSchool" -d "user_id=98" 0.0.0.0:5000/catch_me
