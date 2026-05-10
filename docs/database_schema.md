# Skema Database (Draft)

Berikut adalah tabel-tabel utama yang dibutuhkan untuk aplikasi:

1. **users**
   - `id` (INT, Primary Key)
   - `username` (VARCHAR)
   - `email` (VARCHAR, Unique)
   - `password` (VARCHAR)
   - `avatar_url` (VARCHAR)

2. **roles**
   - `id` (INT, Primary Key)
   - `role_name` (VARCHAR)