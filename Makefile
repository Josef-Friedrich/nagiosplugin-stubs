install: update

update:
	poetry lock
	poetry install

build:
	poetry build

publish:
	poetry build
	poetry publish

format:
	ruff check --select I --fix .
	ruff format

lint:
	ruff check

.PHONY: install update build publish format lint
