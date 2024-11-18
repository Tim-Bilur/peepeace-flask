# Peeace Project

## Deskripsi Proyek

Peeace adalah perangkat cerdas berbasis IoT dan AI untuk mendeteksi indikasi penyakit awal melalui analisis urin. Proyek ini menggunakan beberapa modul untuk prediksi warna, prediksi penyakit, analisis pH, serta kontrol perangkat dan integrasi dengan Firebase. Alur utama terdiri dari proses persiapan data, prediksi warna dan pH, prediksi penyakit, dan tampilan hasil di server.

## Struktur Folder

-   **model/**: Berisi model yang telah dilatih, termasuk file `predict_color.pkl` untuk prediksi warna.
-   **utils/**: Berisi modul utilitas untuk berbagai fungsi pendukung seperti prediksi warna, prediksi penyakit, analisis pH, dan lainnya.

## Struktur File dan Penjelasan

Berikut adalah penjelasan dari file dan fungsinya dalam proyek ini:

### Root

-   **app.py**: File utama untuk menjalankan aplikasi Flask yang menampilkan hasil analisis.
-   **main.py**: File inti yang menghubungkan semua fungsi dari modul yang berbeda dan mengatur alur utama analisis.
-   **README.md**: Dokumentasi proyek.
-   **requirements.txt**: Daftar dependensi Python yang diperlukan untuk menjalankan proyek ini.
-   **.gitignore**: File konfigurasi untuk mengabaikan file dan folder tertentu saat melakukan commit ke repository, seperti `.env` dan `__pycache__`.

### model/

-   **predict_color.pkl**: Model yang telah dilatih untuk prediksi warna berdasarkan data RGB yang diterima dari perangkat.

### utils/

-   **credentials/**

    -   **config.py**: File konfigurasi untuk menyimpan informasi terkait koneksi ke Firebase dan API lainnya yang digunakan dalam proyek.
    -   **firebase2.py**: Modul yang menangani koneksi dan operasi database Firebase, seperti menyimpan dan mengambil data hasil analisis.

-   **func_colorPredict.py**: Modul untuk melakukan prediksi warna berdasarkan model `predict_color.pkl`.
-   **func_disease.py**: Modul untuk melakukan prediksi penyakit berdasarkan data yang dianalisis dari urin.
-   **func_imgkit.py**: Modul untuk mengolah gambar atau menampilkan hasil prediksi dalam bentuk gambar.
-   **func_motor_control.py**: Modul untuk mengontrol perangkat motor, seperti pompa atau aktuator yang mungkin diperlukan dalam perangkat IoT.
-   **func_ph.py**: Modul untuk melakukan analisis dan pengukuran pH berdasarkan data yang diterima dari perangkat.
-   **func_webcam.py**: Modul untuk menangani input dari webcam jika diperlukan dalam proses analisis, seperti mengambil gambar sampel urin.

### .env.example

File ini menyediakan template konfigurasi lingkungan yang dibutuhkan. Pengguna dapat membuat file `.env` berdasarkan template ini untuk menyimpan kredensial dan konfigurasi yang bersifat rahasia.

## Cara Menjalankan Proyek

1. **Instal Dependensi**: Pastikan Anda sudah menginstal dependensi yang terdaftar di `requirements.txt`.

    ```bash
    pip install -r requirements.txt
    ```

2. **Siapkan Konfigurasi Lingkungan (ENV)\***. Buat file `.env` berdasarkan `.env.example` dan isi dengan konfigurasi yang diperlukan

# Pertama Kali Menggunakan Proyek Ini?

Berikut adalah langkah-langkah menjalankan proyek ini:

### Windows

-   Membuat virtual-environment terlebih dahulu

```bash
python -m venv .venv
```

-   Mengaktifkan virtual-environment

```bash
.\venv\Scripts\Activate.ps1
```

-   Menginstal paket dan dependensi

```bash
pip install -r requirements.txt
```

-   Menjalankan proyek

```bash
python app.py
```

### Linux

-   Membuat virtual-environment terlebih dahulu

```bash
python3 -m venv .venv
```

-   Mengaktifkan virtual-environment

```bash
source .venv/bin/activate
```

-   Menginstal paket dan dependensi

```bash
pip install -r requirements.txt
```

-   Menjalankan proyek

```bash
python3 utils/raspi_ph.py

python app.py
```
