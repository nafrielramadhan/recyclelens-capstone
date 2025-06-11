# RecycleLens: Suggests a clear view into recyclability
RecycleLens adalah sebuah aplikasi web yang memanfaatkan deep learning untuk **mendeteksi jenis sampah** dari citra visual.
Tidak hanya dapat mengidentifikasi sampah, RecycleLens juga menyediakan **informasi** penting mengenai **potensi daur ulang dan dampak lingkungan** dari setiap jenis sampah. 
Tujuan utama RecycleLens adalah menjadi alat edukasi yang efektif sehingga dapat mendorong perubahan perilaku masyarakat dalam pengelolaan sampah yang lebih bertanggung jawab, 
dan mendukung Tujuan Pembangunan Berkelanjutan _(SDG)_ 11.

# Fitur
1. Klasifikasi gambar atau foto sampah menjadi enam kategori:
   * kaca _(glass)_
   * kertas _(paper)_
   * kardus _(cardboard)_
   * plastik _(plastic)_
   * logam _(metal)_, dan
   * sampah organik _(trash)_
3. **Informasi edukatif** dari masing-masing jenis sampah tentang:
    * Potensi dan cara daur ulang.
    * Waktu penguraian jika jenis sampah ini tidak didaur ulang dan dibiarkan menumpuk di bumi.
    * Dampak negatif pada bumi.
    * Jejak karbon sampah beserta perbandingannya ketika menghasilkan jumlah karbon yang sama pada aktivitas sehari-hari.
      Poin ini bertujuan untuk memberikan gambaran nyata pada pengguna bahwa mengolah sampah tersebut dapat mengurangi jejak karbon sebanding dengan aktivitas tertentu.

# Cara Kerja
RecycleLens menggunakan model DenseNet121 yang telah dilatih secara ekstensif pada dataset TrashNet dan Kaggle Garbage Classification. 
Setelah Anda mengunggah gambar sampah, model akan memprosesnya dan memberikan kategori sampah yang terdeteksi, beserta informasi tambahan yang relevan.

# Hasil dan Dampak
Model DenseNet121 yang dikembangkan berhasil mencapai akurasi sebesar 97,65% pada data pengujian. 
Akurasi tinggi ini menunjukkan kemampuan sistem yang sangat baik dalam mengidentifikasi berbagai jenis sampah. 
Dengan mengintegrasikan informasi daur ulang dan dampak lingkungan, RecycleLens memperkuat perannya sebagai alat edukasi yang aplikatif, 
diharapkan dapat mendorong peningkatan kesadaran dan partisipasi masyarakat dalam pengelolaan sampah yang lebih bertanggung jawab.

## Eksperimen
| Method            | Model          | Precision | Recall | F1-Score | Accuracy | 
| ----------------- | -------------- |:---------:|:------:|:--------:|:--------:|
| From Scratch      | CNN            |           |        |          |          |
| From Scratch      | CNN            |           |        |   69,06  |          |
| Transfer Learning | MobileNetV2    |           |        |   94,18  |          |
| Transfer Learning | EfficientNetB0 |           |        |   95,81  |          |
| Transfer Learning | DenseNet121    |           |        |   97,65  |          |


# Instalasi dan Penggunaan (Lokal)
1. Clone Repositori
```
git clone https://github.com/filzarahma/recyclelens-capstone.git
cd recyclelens-capstone
```
2. Buat dan aktifkan virtual environment (direkomendasikan)
```
python -m venv venv
source venv/bin/activate  # Untuk Linux/macOS
# venv\Scripts\activate   # Untuk Windows
```
3. Install dependensi yang diperlukan
```
pip install -r requirements.txt
```
4. Jalankan aplikasi Streamlit
```
streamlit run app.py
```

# Struktur Proyek
```
recyclelens-capstone/
├── data/                       # Dataset
├── models/                     # Model yang telah dilatih
├── notebooks/                  # Jupyter notebooks untuk eksplorasi data dan eksperimen model
├── app.py                      # File utama aplikasi Streamlit
├── requirements.txt            # Daftar dependensi Python
└── README.md                   
```

# Cara Penggunaan
1. Upload gambar sampah dengan klik button `upload`
2. 

# Project Member
* Agum Medisa
* Filza Rahma Muflihah
* Muhammad Nafriel Ramadhan
* Oryza Khairunnisa
