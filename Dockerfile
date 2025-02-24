# Start from an official Python image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port that your app will run on (optional, if needed for a web app)
# EXPOSE 5000 

# Run the Python script (adjust the script name if necessary)
CMD ["python", "index.py"]
