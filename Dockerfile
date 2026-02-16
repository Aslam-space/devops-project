# Use a lightweight Python image
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Copy files and install dependencies
COPY . /app
RUN pip install -r requirements.txt

# Open the port
EXPOSE 8080

# Command to run the app
CMD ["python", "app.py"]