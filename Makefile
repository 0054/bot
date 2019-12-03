SHELL := /bin/bash
.ONSHELL:
.PHONY: install
install:
	source .venv/bin/activate; \
		pip install -r bot/requirements.txt

.PHONY: requirements
requirements:
	source .venv/bin/activate; \
		pip freeze > bot/requirements.txt

.PHONY: up-dev-server
up-dev-server:
	source .venv/bin/activate; \
		python3 bot/bot.py

.PHONY: run
run:
	docker-compose -f docker/docker-compose.yml up -d

.PHONY: stop
stop:
	docker-compose -f docker/docker-compose.yml stop

.PHONY: rm
rm:
	docker-compose -f docker/docker-compose.yml stop
	docker-compose -f docker/docker-compose.yml rm
