ifneq (,$(wildcard .env))
include .env
export
endif

PYTHON ?= $(CURDIR)/.venv/bin/python

.PHONY: help db-up db-down db-logs db-shell migrate makemigrations runserver

help:
	@printf "make db-up            Start PostgreSQL container\n"
	@printf "make db-down          Stop containers\n"
	@printf "make db-logs          Tail PostgreSQL logs\n"
	@printf "make db-shell         Open psql shell in DB container\n"
	@printf "make migrate          Run Django migrations\n"
	@printf "make makemigrations   Create Django migration files\n"
	@printf "make runserver        Start Django dev server\n"
	@printf "make create-superuser Create Django superuser\n"

db-up:
	docker compose up -d db

db-down:
	docker compose down

db-logs:
	docker compose logs -f db

db-shell:
	docker exec -it mini-crm-db psql -U $(POSTGRES_USER) -d $(POSTGRES_DB)

migrate:
	set -a; [ -f .env ] && . ./.env; set +a; cd apps/api && $(PYTHON) manage.py migrate

makemigrations:
	set -a; [ -f .env ] && . ./.env; set +a; cd apps/api && $(PYTHON) manage.py makemigrations

runserver:
	set -a; [ -f .env ] && . ./.env; set +a; cd apps/api && $(PYTHON) manage.py runserver

create-superuser:
	set -a; . .env; set +a; cd apps/api && ../../.venv/bin/python manage.py createsuperuser
