FROM python:3.9-slim

WORKDIR /app

ENV PYTHONPATH=/app

# System dependencies (safe minimal version)
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    ca-certificates \
    gcc \
    unixodbc \
    unixodbc-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app ./app

EXPOSE 8000

CMD ["pytest"]

CMD ["python", "app/main.py"]