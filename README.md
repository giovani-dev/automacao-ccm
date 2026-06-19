# automacao-ccm

Development & CI
----------------

This repository uses `mise` to manage tool versions (see `mise.toml`) and `Poetry` for dependency management.

Local setup:

```bash
# install tools declared in mise.toml
mise install

# install project dependencies
poetry install --no-interaction

# run tests
poetry run pytest -q

# run linters
poetry run mypy src
poetry run pylint src
poetry run black --check .
```

Docker
------

Build the development image (Dockerfile installs `mise` and `poetry`):

```bash
docker compose -f docker/docker-compose.yml build
docker compose -f docker/docker-compose.yml up
```

CI
--

The GitHub Actions workflow uses `jdx/mise-action@v2` to install tools from `mise.toml`, then runs `poetry install` and the checks (`mypy`, `pylint`, `black`, `pytest`).
