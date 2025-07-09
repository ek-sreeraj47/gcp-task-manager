# Use official Python base image
FROM python:3.9-slim

# Set working directory inside container
WORKDIR /app

# Copy only required files
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY . .

# Expose port 8080 to Cloud Run
EXPOSE 8080

# Set the startup command
CMD ["python", "app.py"]

