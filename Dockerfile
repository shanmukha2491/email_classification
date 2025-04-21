FROM python:3.9-slim

# Install system dependencies needed for building the package (including build-essential)
RUN apt-get update && apt-get install -y \
    build-essential \
    python3-dev \
    libblas-dev \
    liblapack-dev \
    gfortran \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy the current directory contents into the container
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the correct port
EXPOSE 7860

# Run the FastAPI app using Uvicorn
CMD ["uvicorn", "app.api:app", "--host", "0.0.0.0", "--port", "7860"]
