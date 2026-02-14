FROM python:3.13-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    libpq-dev \
    postgresql-client \
    libheif-dev \
    libde265-dev \
    libx265-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

RUN apt-get update && apt-get purge -y \
    gcc \
    g++ \
    libpq-dev \
    && apt-get autoremove -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY . .

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENV PYTHONPATH=/app
ENV PYTHONUNBUFFERED=1

EXPOSE 5000

# Use entrypoint script
ENTRYPOINT ["/entrypoint.sh"]

# Run the application
CMD ["uvicorn", "--factory", "src.main:get_app", "--host", "0.0.0.0", "--port", "5000"]
