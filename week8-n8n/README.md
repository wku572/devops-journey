# Week 8: n8n Automation

Self-hosted n8n, run with Docker Compose.

## Run it
```
docker compose up -d
```
Open http://localhost:5678 and create a local owner account.

## Notes
- Workflows and credentials live in the `n8n-data` volume.
- `docker compose down` keeps them. `docker compose down -v` deletes them.
- The timezone is set in `compose.yaml`, and schedules follow it.
- n8n opens on the Assistant page. Your workflows are under Overview.
