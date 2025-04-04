# Fullstack Docker App

A Dockerized fullstack app using React, Flask, and PostgreSQL.

## Services

- frontend: React app served via NGINX
- backend: Flask API with PostgreSQL
- db: PostgreSQL database

## Deploy (Docker Swarm)

```bash
docker stack deploy -c docker-compose.yml fullstack
