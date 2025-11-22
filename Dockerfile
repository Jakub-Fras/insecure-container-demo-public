# Slightly older Python base image (will have OS vulns)
FROM python:3.10-slim-bullseye

# Work as root (bad practice)
WORKDIR /app

# Hardcoded "secret" in env (intentionally insecure)
ENV DB_PASSWORD=SuperInsecurePassword123!

# Install extra tools we don't strictly need (increases attack surface)
RUN apt-get update && \
    apt-get install -y curl vim && \
    rm -rf /var/lib/apt/lists/*

# Copy vulnerable Python dependencies from repo root
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the vulnerable app (everything in the repo)
COPY . .

# App listens on port 8080
EXPOSE 8080

# Still running as root (intentionally insecure)
CMD ["python", "main.py"]
