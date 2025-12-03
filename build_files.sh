
#!/bin/bash

set -e

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Running migrations..."
python manage.py makemigrations --noinput || true
python manage.py migrate --noinput || true

echo "Collecting static files..."
python manage.py collectstatic --noinput --clear

echo "Copying static files to build directory..."
mkdir -p staticfiles_build
cp -r staticfiles/* staticfiles_build/

echo "Build completed successfully!"