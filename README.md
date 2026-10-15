# DevOps Journey

![CI](https://github.com/wku572/devops-journey/actions/workflows/ci.yml/badge.svg)

My 90-day plan to learn Linux, Automation, DevOps, and Cloud, built in public.

## Progress
- [x] Week 1: Linux basics (cheat sheet)
- [x] Week 2: Bash scripting (backup script with logging and cron)
- [x] Week 3: Git and GitHub (SSH, branches, pull requests, merge conflicts)
- [x] Week 4: Python basics (API script with requests and venv)
- [x] Week 5: Docker (containerized the Python script)
- [x] Week 6: Docker Compose (Flask app and Postgres)
- [x] Week 7: CI/CD with GitHub Actions (lint, tests, Docker build)
- [x] Week 8: Automation project (n8n workflow with schedule and Telegram)
- [ ] Weeks 9-12: Cloud, Terraform, portfolio project

## What's inside
- `linux-cheatsheet.md` and `git-cheatsheet.md`: commands and workflows in my own words
- `week2-bash/`: Bash scripts, including a backup script with logging
- `week4-python/`: a GitHub API script with tests and a Dockerfile
- `week6-compose/`: a Flask app and Postgres database run with Docker Compose
- `week8-n8n/`: self-hosted n8n and an exported workflow that sends a daily Telegram report
- `.github/workflows/ci.yml`: pipeline that lints, tests, and builds images on every push

## How the pipeline works
Every pull request runs three jobs: `lint` (flake8 and Bash syntax checks),
`test` (pytest with a mocked API), and `docker-build`, which only starts after
the first two pass.

## About me
I am learning automation and DevOps from scratch with free resources and
hands-on projects. My goal is to build a portfolio that shows real skills
and to earn an entry-level cloud or DevOps certification.
