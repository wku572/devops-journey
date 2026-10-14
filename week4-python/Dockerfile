FROM python:3.12-slim

WORKDIR /app

# Install dependencies first so Docker can cache this layer
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Then copy the script
COPY fetch_github.py .

ENTRYPOINT ["python", "/app/fetch_github.py"]
