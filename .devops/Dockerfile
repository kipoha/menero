FROM ghcr.io/astral-sh/uv:python3.11-alpine

ENV PYTHONUNBUFFERED=1

WORKDIR /opt/menero-new

COPY pyproject.toml ./
COPY uv.lock ./

RUN uv sync

COPY . .

RUN chmod +x /opt/menero-new/entrypoints/*.sh
