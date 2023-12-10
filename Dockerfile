# Use the official TensorFlow image as the base image
FROM tensorflow/tensorflow:latest

# Copy the model file into the container
COPY model.h5 /app/model.h5

# Copy the app.py file into the container
COPY app.py /app/app.py

# Set the working directory to /app
WORKDIR /app

# Install Flask and other dependencies
RUN pip install Flask

# Expose the port on which the application will run
EXPOSE 8080

# Define the command to run the application
CMD ["python", "app.py"]
