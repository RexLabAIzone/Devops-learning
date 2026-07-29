#!/bin/bash

set -e

echo "=====pull code===="
git pull

echo "=====build image=="
docker compose build

echo "=====restart servie==="
docker compose up -d

echo "======status====="
docker compose ps
