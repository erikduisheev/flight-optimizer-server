#!/bin/sh

set -o errexit

python /optimizer/manage.py migrate

exec "$@"