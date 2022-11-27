#!/usr/bin/env bash

echo "Start migrations..."
python test_stripe/manage.py migrate

echo "Start test_stripe..."
gunicorn test_stripe.test_stripe.wsgi:application --bind 0.0.0.0:8000