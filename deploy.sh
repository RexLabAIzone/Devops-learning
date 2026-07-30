#!/bin/bash

set -e

echo "=====pull code===="
git pull

echo "=====build image=="
docker compose -f docker-compose.prod.yml build

echo "=====restart servie==="
docker compose -f docker-compose.prod.yml up -d

echo "======status====="
docker compose -f docker-compose.prod.yml ps
