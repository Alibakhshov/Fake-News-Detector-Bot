# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Install any dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the bot will run on (if it uses one)
# EXPOSE 8000  # Uncomment if your bot uses a specific port

# Run bot.py when the container launches
CMD ["python", "bot.py"]
