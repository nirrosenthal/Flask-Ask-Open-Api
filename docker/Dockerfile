FROM ubuntu:20.04

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    && apt-get clean

WORKDIR /app

COPY ../src/ ./src/
COPY ../migration/alembic/ ./alembic/
COPY ../migration/alembic.ini .
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt
