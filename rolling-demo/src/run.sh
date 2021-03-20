#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

# Put in background
$DIR/ready.sh &

/opt/app-root/bin/python app.py