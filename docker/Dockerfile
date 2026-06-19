FROM ubuntu:22.04
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update \
    && apt-get install -y --no-install-recommends curl ca-certificates build-essential git python3-venv python3-distutils python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Install mise
RUN curl -sSf https://mise.jdx.dev/install.sh | sh
ENV PATH="/root/.local/bin:${PATH}"

# Install tools declared in mise.toml (Poetry)
RUN mise install || true

WORKDIR /app

# Copy pyproject and lock first to leverage Docker cache
COPY pyproject.toml poetry.lock* /app/

# Install project dependencies via Poetry (installed by mise)
RUN if command -v poetry >/dev/null 2>&1; then poetry install --no-interaction; else python -m pip install --upgrade pip && pip install poetry && poetry install --no-interaction; fi

COPY . /app

CMD ["poetry", "run", "python", "src/main.py"]
