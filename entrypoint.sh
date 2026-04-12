#!/bin/sh

echo "⏳ Waiting for database..."

while ! nc -z postgres 5432; do
  sleep 0.5
done

echo "✅ Database is ready!"

echo "📦 Applying migrations..."
python manage.py migrate --noinput

echo "📦 Collecting static..."
python manage.py collectstatic --noinput

echo "🚀 Starting Gunicorn..."
gunicorn config.wsgi:application --bind 0.0.0.0:8000 --workers 3