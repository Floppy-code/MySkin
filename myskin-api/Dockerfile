FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY requirements.txt .
RUN python -m pip install -r requirements.txt

COPY . /app

# Creates a non-root user with an explicit UID and adds permission to access the /app folder.
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser

WORKDIR /app

EXPOSE 8000
# Provides defaults for an executing container; can be overridden with Docker CLI.
CMD ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:8000", "--timeout", "600", "main:app"]