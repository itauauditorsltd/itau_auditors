#!/bin/bash

# Exit immediately if a command exits with a non-zero status.
set -e

# Ensure pip is installed
echo "Ensuring pip is installed..."
python3.9 -m ensurepip --upgrade
echo "Upgrading pip..."
python3.9 -m pip install --upgrade pip

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Make and apply migrations
echo "Making migrations..."
python3.9 manage.py makemigrations
echo "Applying migrations..."
python3.9 manage.py migrate

# Collect static files
echo "Collecting static files..."
python3.9 manage.py collectstatic --noinput
