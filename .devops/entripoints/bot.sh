#!/bin/sh
export PYTHONPATH=/opt/services/project:$PYTHONPATH

echo "Start migrations"
uv run alembic upgrade head

cd /opt/menero-new/src

echo "Start bot"
uv run main.py
