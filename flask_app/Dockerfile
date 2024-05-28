# Use the official Python image as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y nginx

# Copy the requirements file into the container
COPY requirements.txt .
RUN apt-get update && apt-get install -y \
    gcc \
    build-essential \
    libssl-dev \
    libffi-dev \
    python3-dev \
    nginx && \
    rm -rf /var/lib/apt/lists/*
# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Flask application code into the container
COPY . .

# Expose the port that Uvicorn will listen on
EXPOSE 8000

# Run Uvicorn when the container launches
CMD ["uwsgi","--ini", "run.ini"]