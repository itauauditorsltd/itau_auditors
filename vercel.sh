#!/bin/bash

# This script ensures we use Python 3.9
yum install -y python39 python39-pip || true
python3.9 -m pip install --upgrade pip
python3.9 -m pip install -r requirements.txt