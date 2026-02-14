#!/bin/sh
set -e
echo "Running database migrations..."
alembic upgrade head

if [ $? -ne 0 ]; then
    echo "ERROR: Database migrations failed!"
    exit 1
fi

echo "Migrations completed successfully!"
echo "Starting application..."
exec "$@"

