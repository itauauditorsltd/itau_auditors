#!/bin/bash

# Ensure pip is installed
python3.9 -m ensurepip --upgrade
python3.9 -m pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt

# Run migrations
python3.9 manage.py migrate

# Collect static files
python3.9 manage.py collectstatic --noinput
