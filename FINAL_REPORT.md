# Final Report - Kontribusi Individu Proyek CAKRA

**Nama:** Ilham Dimas Ramadhan
**NPM:** 2313020238
**Peran:** Backend Developer
**Proyek:** CAKRA (CCTV Lalu Lintas Karesidenan Kediri)

## 1. Ringkasan Eksekutif
Selama 16 minggu masa pengembangan sistem CAKRA, saya bertanggung jawab penuh atas arsitektur sisi server (Backend) dan manajemen basis data. Fokus utama saya adalah memastikan aliran data streaming CCTV dari wilayah Kediri, Tulungagung, dan Blitar dapat disajikan secara efisien dan aman melalui API kepada tim Frontend, serta menjamin persistensi data di lingkungan *production* menggunakan teknologi kontainerisasi.

## 2. Kontribusi Spesifik (Backend Developer)
Sebagai Backend Developer, berikut adalah rincian teknis dari kontribusi yang saya berikan pada repositori kelompok:

*   **Pengembangan Arsitektur API (NestJS):** 
    Membangun fondasi backend menggunakan *framework* NestJS. Saya menyusun *routing*, *controllers*, dan *services* untuk menangani *request* data operasional kamera dan status lalu lintas dari klien (PWA).
*   **Manajemen Basis Data (MySQL):** 
    Merancang skema relasional database dan menghubungkannya dengan aplikasi NestJS. Mengatur entitas untuk menyimpan metadata CCTV dan kredensial akses pengguna.
*   **Kontainerisasi Sistem (Docker):** 
    Merancang `Dockerfile` khusus untuk sisi backend dengan mengimplementasikan proses *build* yang efisien. Membantu penyusunan `docker-compose.yml` untuk lingkungan *development*.
*   **Persistensi Data & Persiapan Rilis (Production-Ready):** 
    Mengamankan data aplikasi dari risiko kehilangan saat pembaruan sistem dengan mengonfigurasi *Named Volume* (`cakra_db_data:/var/lib/mysql`) pada MySQL. Melakukan proses *push image* backend ke GitHub Container Registry (GHCR) agar aplikasi siap ditarik oleh sistem orkestrasi *production*.

## 3. Daftar Commit Terbaik (Highlight Portofolio)
Berikut adalah rekam jejak (*commit history*) yang merepresentasikan kontribusi teknis terbaik saya dalam repositori tim:

1.  **[Add project architecture documentation](https://github.com/Zulfachmad/Cakra---CCTV-Lalu-lintas-Karesidenen-Kediri/commit/8301b48e8bc616624c1857f6e09f3acdd4b90675)**
    *Deskripsi:* Menyusun dokumentasi awal mengenai arsitektur proyek agar alur sistem CAKRA tergambar dengan jelas bagi seluruh anggota tim.
2.  **[Format API documentation for better readability](https://github.com/Zulfachmad/Cakra---CCTV-Lalu-lintas-Karesidenen-Kediri/commit/c84dfe71b8d5176d5a27af8860ade7f6bf9e72d1)**
    *Deskripsi:* Merapikan format dokumentasi API (*API Contract*) sehingga mudah dibaca dan diimplementasikan secara akurat oleh Frontend Developer.
3.  **[chore(backend): sinkronisasi dependensi NestJS dan verifikasi .gitignore](https://github.com/Zulfachmad/Cakra---CCTV-Lalu-lintas-Karesidenen-Kediri/commit/1646a822ba8daca307ad26b457b171098682b86f)**
    *Deskripsi:* Mengatur ulang dependensi *framework* NestJS dan memastikan file konfigurasi lokal tidak ikut ter-push ke *public repository* melalui `.gitignore`.
4.  **[chore(backend): tambah Dockerfile dan inisiasi environment variables](https://github.com/Zulfachmad/Cakra---CCTV-Lalu-lintas-Karesidenen-Kediri/commit/7607e8c9688648544037afca8bf2e6a6b3019216)**
    *Deskripsi:* Pengemasan aplikasi backend ke dalam *container* mandiri serta pengaturan variabel lingkungan (*env*) untuk keamanan kredensial.
5.  **[chore(backend): tambah named volume untuk database MySQL](https://github.com/Zulfachmad/Cakra---CCTV-Lalu-lintas-Karesidenen-Kediri/commit/464217b942d24e09ca4475b7b26ebe157ea61297)**
    *Deskripsi:* Konfigurasi krusial pada instruksi Docker untuk memastikan data rekaman CCTV dan *user* persisten dan tidak hilang saat sistem di-*restart* atau di-*update*.

## 4. Kesimpulan
Proyek ini memberikan pemahaman mendalam mengenai siklus hidup pengembangan perangkat lunak (SDLC) modern. Saya tidak hanya belajar menulis kode server yang fungsional, tetapi juga memahami pentingnya mengelola integritas kode melalui Git, menyelesaikan masalah *portability* menggunakan Docker, dan pentingnya sinkronisasi alur kerja dengan peran Product Lead dan Frontend Developer.
