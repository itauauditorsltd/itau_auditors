#!/bin/bash

set -e

# Install dependencies
pip install -r requirements.txt

# Make and apply migrations
python3.9 manage.py makemigrations
python3.9 manage.py migrate

# Collect static files (this command is used to gather static files)
python3.9 manage.py collectstatic --noinput

# No need to handle `staticfiles_build` if using S3 for static files
# Create the directory if it's needed
mkdir -p staticfiles_build

# Copy collected static files to the `staticfiles_build` directory
cp -r static/* staticfiles_build/
