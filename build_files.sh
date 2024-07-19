#!/bin/bash

# Exit immediately if a command exits with a non-zero status.
set -e

# Ensure pip is installed
python3.9 -m ensurepip --upgrade
python3.9 -m pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt

# Make and apply migrations
python3.9 manage.py makemigrations
python3.9 manage.py migrate

# Collect static files
python3.9 manage.py collectstatic --noinput --clear

# Ensure the output directory exists
mkdir -p staticfiles_build
