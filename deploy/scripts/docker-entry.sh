#!/bin/sh

# set -e

ENV PATH="/venv/bin:${PATH}"

exec python manage.py runserver 0.0.0.0:$1
