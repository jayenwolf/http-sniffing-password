# HTTP Credential Sniffing & Packet Analysis Lab

Proyek dokumentasi analisis lalu lintas jaringan dan pengujian kerentanan transmisi data teks polos (*plaintext*) menggunakan Python HTTP Server dan Wireshark di lingkungan Kali Linux.

---

## 1. Tujuan Lab
* Memahami cara kerja pengiriman data otentikasi pada layer aplikasi menggunakan metode HTTP `POST`.
* Mempraktikkan teknik *packet sniffing* dan rekonstruksi sesi (*stream reassembly*) menggunakan Wireshark.
* Membuktikan secara visual kerentanan transmisi data tanpa enkripsi (*cleartext*) terhadap risiko penyadapan *Man-in-the-Middle* (MitM).

---

## 2. Lingkungan Pengujian (Lab Environment)
* **Sistem Operasi:** Kali Linux (VirtualBox)
* **Packet Analyzer:** Wireshark
* **Backend:** Python 3 (`http.server`, `HTTPServer`, `SimpleHTTPRequestHandler`)
* **Interface Jaringan:** Loopback (`lo`)
* **Port Layanan:** `8080` (HTTP)

---

## 3. Komponen Proyek
* `index.html`: Halaman antarmuka formulir login sederhana dengan atribut `method="POST" action="/login"`.
* `server.py`: Server HTTP lokal berbasis Python yang menangani request `POST`, mengekstrak parameter body, dan mengembalikan status respon `200 OK`.

---

## 4. Metodologi & Langkah Kerja

1. **Menjalankan Web Server Lokal:**
   ```bash
   python3 server.py
