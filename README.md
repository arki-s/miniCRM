# Mini CRM Monorepo

![API CI](https://github.com/arki-s/mini-crm-api/actions/workflows/api-ci.yml/badge.svg)

A minimal monorepo for a CRM product with a Django API today and a planned
Next.js frontend.

## Purpose

This project is a small CRM backend built to practice a real-world backend stack
(Django REST Framework, JWT authentication, PostgreSQL)
used in my current work.

The focus is not feature completeness, but:

- API design and responsibility boundaries
- Data modeling and query patterns
- Authentication and authorization flow
- Frontend–backend integration via REST APIs

This repository now keeps both application entrypoints in one place so API and
web can evolve independently while sharing CI and repository settings.

## Planned Features (MVP)

- JWT-based authentication
- Deal CRUD API
- Deal list with filters
  - status (multiple)
  - keyword search (deal name / client name)
  - date range (created / updated)
- Activity timeline per deal
- Create and update activities
- Owner-based data access control

## API Overview (Planned)

### Auth

- `POST /auth/login`
- `POST /auth/refresh`

### Deals

- `GET /deals`
- `POST /deals`
- `GET /deals/{id}`
- `PATCH /deals/{id}`
- `DELETE /deals/{id}` (optional)

### Activities

- `GET /deals/{id}/activities`
- `POST /deals/{id}/activities`
- `PATCH /activities/{id}`
- `DELETE /activities/{id}`

## Apps

- `apps/api`: Django REST Framework API
- `apps/web`: reserved for the future Next.js frontend

## Tech Stack

- Python 3.12+
- Django
- Django REST Framework
- SQLite (local development)
- Ruff (linting)
- GitHub Actions (API CI today, Web CI later)

## Project Structure

```text
mini-crm-api/
├── apps/
│   ├── api/
│   │   ├── config/          # Django project settings
│   │   ├── crm/             # Core CRM app (models, views, serializers)
│   │   ├── manage.py
│   │   ├── pyproject.toml
│   │   └── requirements.txt
│   └── web/                 # Reserved for Next.js
├── .github/workflows/
│   └── api-ci.yml
└── README.md
```

## Development Setup

### 1. Local Python setup

- python -m venv .venv
- source .venv/bin/activate
- pip install -r apps/api/requirements.txt

### 2. Database setup with Docker

- cp .env.example .env
- make db-up

### 3. Run Django against PostgreSQL

- make migrate
- make runserver

If you want to stay on SQLite for quick experiments, set `DB_ENGINE=sqlite` in `.env`
or simply run without loading `.env`.

The default Docker-exposed PostgreSQL port is `5433` so it does not collide with an
already-running local PostgreSQL on `5432`.

## CI

- `api-ci.yml` runs only when `apps/api/**` or the API workflow changes
- Web CI will be added when `apps/web` is scaffolded

## Status

🚧 Work in Progress

- Django + DRF project initialized
- Health check endpoint implemented
- API CI split out for the monorepo layout
- Core models and APIs under development
