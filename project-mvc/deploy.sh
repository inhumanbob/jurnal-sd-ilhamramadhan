#!/bin/bash
echo "Memulai proses deployment versi 2.0..."

echo "1. Menarik image terbaru dari registry..."
docker pull ghcr.io/inhumanbob/mvc-app-ilham:v2-prod

echo "2. Menjalankan kontainer versi 2.0 di port 8081..."
docker run -d --name app-v2 -p 8081:5000 ghcr.io/inhumanbob/mvc-app-ilham:v2-prod

echo "3. Menghentikan dan menghapus kontainer versi lama (app-v1)..."
docker stop app-v1
docker rm app-v1

echo "Deployment sukses! Aplikasi versi 2.0 sudah berjalan."