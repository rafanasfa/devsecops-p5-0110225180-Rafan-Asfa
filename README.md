# DevSecOps Python User API Service

Aplikasi REST API sederhana berbasis Python (Flask) yang dibuat untuk pemenuhan tugas praktikum DevSecOps.

## 1. Deskripsi Aplikasi & Fungsi
Aplikasi ini menyediakan layanan REST API sederhana untuk pengelolaan data pengguna (User Management Service) dengan fungsi:
- Endpoint health check (`/`)
- Endpoint fetching daftar pengguna (`/api/users`)
- Endpoint pencarian pengguna berdasarkan ID (`/api/users/<id>`)

## 2. Bahasa & Framework
- **Bahasa Pemrograman:** Python 3.10+
- **Framework Web:** Flask
- **Testing Framework:** pytest

## 3. Cara Menjalankan Aplikasi

### Lokal
1. Install dependensi:
   ```bash
   pip install -r requirements.txt