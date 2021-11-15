#!/bin/bash

ssh ids3 'cd /data/deploy-ids-tests/biohackathon2021 ; git pull ; docker-compose build --no-cache ; docker-compose down ; docker-compose up -d --force-recreate'
