# Gunakan image resmi Python sebagai base image
FROM python:3.8

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Buat dan pindahkan ke direktori kerja /app
WORKDIR /app

# Salin file requirements.txt ke dalam container
COPY requirements.txt /app/

# Install dependensi
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Salin seluruh konten ke dalam container
COPY . /app/

# Eksekusi perintah ketika container dijalankan
CMD ["python", "app.py"]
