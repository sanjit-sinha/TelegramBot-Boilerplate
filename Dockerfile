# Use an official Python runtime as the base image.
# https://hub.docker.com/_/python
FROM python:3.10-slim

# Set the working directory in the container.
WORKDIR /app

# Allowing read, write, and execute permissions .
RUN chmod 777 /app

# Copy the requirements.txt file to the container.
COPY requirements.txt .

# Install the Python dependencies.
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Python script to the container.
COPY . .

# Set the default command to run when the container starts.
CMD ["python3", "-m", "TelegramBot"]
