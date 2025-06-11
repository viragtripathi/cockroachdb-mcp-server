FROM python:3.11-slim

WORKDIR /app

# Install uv globally and install deps into system Python
COPY pyproject.toml .
RUN pip install --no-cache-dir uv && uv pip install --system .

# Copy app
COPY ./app ./app
COPY ./schema ./schema

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
#CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
