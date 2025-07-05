# Use the official Python image as the base image
FROM python:alpine 

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY . .
RUN chmod +x start.sh
# Expose the port FastAPI will run on
EXPOSE 8000
# Set environment variables
# Command to run the a  pplication
CMD ["sh", "start.sh"]