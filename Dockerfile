# Use python version for our base image
FROM python:3.14.4

# Goes to the app directory
WORKDIR /app

# Install dependencies system 
RUN apt-get update && apt-get install -y --no-install-recommends \ 
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy file requirements.txt
COPY requirements.txt .

# Install library python
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of our app into the container
COPY . .

# Set port environment variabel
EXPOSE 5000

# Run to the app main
CMD ["python", "app.py"]

