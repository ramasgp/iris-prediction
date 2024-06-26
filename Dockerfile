# Gunakan image Python sebagai base image
FROM python:3.9-slim

# Set environment variable untuk buffering Python output
ENV PYTHONUNBUFFERED True

# Setel direktori kerja di dalam container
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

# Install dependencies yang terdaftar di requirements.txt
RUN pip install -r requirements.txt

ENV FLASK_APP=main.py

# Jalankan aplikasi Flask menggunakan Gunicorn
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 main:app
