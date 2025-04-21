# Use official Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy code into container
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

# Expose port
EXPOSE 7860

# Run the FastAPI app using Uvicorn
CMD ["uvicorn", "app.api:app", "--host", "0.0.0.0", "--port", "7860"]
