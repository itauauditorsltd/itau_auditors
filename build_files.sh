#!/bin/bash

set -e

# Install dependencies
pip install -r requirements.txt

# Make and apply migrations
python3.9 manage.py makemigrations
python3.9 manage.py migrate

# Collect static files
python3.9 manage.py collectstatic --noinput --clear

# Create the directory if needed
mkdir -p staticfiles_build

# Copy ALL collected static files to staticfiles_build
cp -r staticfiles/* staticfiles_build/