FROM python:3.11-slim as base

ENV PYTHONUNBUFFERED 1
ENV PYTHONFAULTHANDLER 1
ENV PYTHONHASHSEED random
ENV PIP_NO_CACHE_DIR=1
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV POETRY_VERSION=1.3.2

WORKDIR /app

COPY ./requirements.txt .
RUN pip install -r requirements.txt

# CMD ["./deploy/scripts/docker-entry.sh", "8000"]