#!/bin/sh

set -o errexit

python /app/manage.py migrate

exec "$@"