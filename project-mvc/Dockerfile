# STAGE 1: Builder (Alat Tukang)
FROM python:3.9-slim AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --user -r requirements.txt

# STAGE 2: Production (Hasil Jadi menggunakan Alpine yang sangat kecil)
FROM python:3.9-alpine
WORKDIR /app

# Menyalin hasil instalasi dari stage builder
COPY --from=builder /root/.local /root/.local
# Menyalin file kode aplikasi kita (app.py)
COPY . .

ENV PATH=/root/.local/bin:$PATH
# Memastikan variabel lingkungan M12 tetap ada untuk penugasan D2
ENV APP_USER="Ilham Dimas Ramadhan"

CMD ["python", "app.py"]