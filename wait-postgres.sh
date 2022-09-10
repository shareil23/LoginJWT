#!/bin/sh

while ! nc -z mercari_postgres_auth_servcies 5432; do
    echo "Postgres is unavailable - sleeping"
    sleep 3;
done

echo "Postgres is up"