# Use the official Python base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file to the working directory
COPY requirements.txt .
COPY src/prediction.py ./src/
COPY src/Monitoring.py ./src/

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the necessary files to the working directory
COPY main.py .
COPY artifacts/Stroke.pkl ./artifacts/
COPY Reports/*.html ./Reports/

# Expose the port on which the Streamlit app will run
EXPOSE 8501

# Set the entrypoint command to run the Streamlit app
CMD ["streamlit", "run", "--server.port", "8501", "main.py"]
