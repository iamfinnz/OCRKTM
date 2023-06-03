# Use an official Python runtime as the base image
FROM python:3.9-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

RUN apt update -y && apt install python3-pip python3-flask tesseract-ocr -y

# Install the application dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Flask application code to the container
COPY . .

# Expose the port on which the Flask app will run
EXPOSE 5000

# Set environment variables, if necessary
# ENV MY_ENV_VARIABLE value

ENV FLASK_APP "app.py"

# Set the command to run the Flask application
CMD ["flask", "run", "--host=0.0.0.0"]
