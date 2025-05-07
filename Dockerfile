# Gunakan Python image sebagai base
FROM python:3.9-slim

# Set working directory di dalam container
WORKDIR /app

# Copy requirements.txt ke dalam container
COPY requirements.txt .

# Install dependensi
RUN pip install --no-cache-dir -r requirements.txt

# Salin semua file aplikasi ke dalam container
COPY . .

# Port yang akan digunakan di container
EXPOSE 8000

# Perintah untuk menjalankan aplikasi FastAPI
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
