#!/bin/bash
set -e

echo "Stopping old containers..."
docker-compose down -v

echo "Building and starting new containers..."
docker-compose up --build -d

echo "Waiting for PostgreSQL to be ready..."
until docker exec fastapi_inv_pg pg_isready -U inventory_user; do
  sleep 2
done

echo "Schema initialized."
echo "Project setup complete. FastAPI running at http://localhost:8000"
