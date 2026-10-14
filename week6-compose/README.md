# Week 6: Docker Compose

A small Flask web app that counts page visits in a Postgres database, run as
two containers with Docker Compose.

## What's here
- `app.py`: the Flask app. It creates a `visits` table and records each request.
- `Dockerfile`: builds the web image from `python:3.12-slim`.
- `compose.yaml`: defines the `web` and `db` services, a named volume, and a
  database healthcheck.
- `.env.example`: template for the settings Compose needs.

## How to run
```
cp .env.example .env      # then set your own password in .env
docker compose up -d --build
curl localhost:5001
docker compose down       # add -v to also delete the data volume
```

## How it works
- Compose puts both services on one private network, so the app reaches the
  database by the name `db`.
- The database port is not published to the host. Only the web app is, on
  port 5001.
- `depends_on` with a healthcheck makes the app wait until Postgres is ready.
- The named volume `db-data` keeps the data after containers are removed.
- Credentials live in `.env`, which is ignored by Git.

## What I learned
- A service name works as a hostname on a Compose network.
- Containers on Docker's default network can't find each other by name.
- A healthcheck is more reliable than just starting services in order.
- `docker compose down` keeps data, and `down -v` deletes it.
