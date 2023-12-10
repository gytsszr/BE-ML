# Gunakan base image yang mendukung Python dan TensorFlow
FROM python:3.8

# Set working directory
WORKDIR /app

# Salin file dependencies ke working directory
COPY requirements.txt .

# Install dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Salin model H5 ke working directory
COPY model.h5 .

# Salin file Python aplikasi Anda ke working directory
COPY app.py .

# Ekspose port yang digunakan oleh aplikasi
EXPOSE 8080

# Jalankan aplikasi saat container dimulai
CMD ["python", "app.py"]
