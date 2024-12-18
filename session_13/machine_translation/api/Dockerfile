# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8000 for the FastAPI application
EXPOSE 8000

# Command to run the FastAPI app
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
