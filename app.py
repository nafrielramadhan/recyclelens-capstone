import streamlit as st
import numpy as np
from PIL import Image
import tensorflow as tf
from utils.recycle_info import recycle_guide

# Load model
@st.cache_resource
def load_model():
    return tf.keras.models.load_model('model/DenseNet121_trashnetmerged_best_model.h5')

model = load_model()

# Kategori
CATEGORIES = ['cardboard', 'glass', 'metal', 'paper', 'plastic', 'trash']

# Fungsi Prediksi
def predict_image(img):
    img = img.convert("RGB")
    img = img.resize((224, 224))
    img_array = np.array(img) / 255.0
    img_array = img_array.reshape(1, 224, 224, 3)
    pred = model.predict(img_array)
    idx = np.argmax(pred)
    confidence = float(np.max(pred))
    return CATEGORIES[idx], confidence

# Halaman Utama
st.set_page_config(page_title="RecycleLens", layout="wide")
st.title("♻️ RecycleLens")
st.markdown("Suggests a clear view into recyclability")

# Tab Navigasi
tab1, tab2, tab3, tab4 = st.tabs(["🔍 Deteksi Sampah", "📦 Kategori Sampah", "📷 Panduan", "🧠 Tentang Kami"])

# Tab 1: Deteksi Sampah
with tab1:
    st.subheader("🔍 Unggah atau Ambil Gambar Sampah")

    option = st.radio("Pilih metode input gambar:", ["📁 Upload File", "📷 Kamera"], horizontal=True)

    image = None 

    if option == "📁 Upload File":
        uploaded_file = st.file_uploader("Upload gambar dari perangkat", type=["jpg", "jpeg", "png"])
        if uploaded_file:
            image = Image.open(uploaded_file)

    elif option == "📷 Kamera":
        camera_image = st.camera_input("Ambil gambar dari kamera")
        if camera_image:
            image = Image.open(camera_image)

    if image:
        label, confidence = predict_image(image)
        info = recycle_guide[label]

        col1, spacer, col2 = st.columns([1, 0.1, 2])
        with col1:
            st.image(image, caption="Gambar yang Diambil", use_container_width=True)
        with col2:
            st.success(f"Prediksi Kategori Sampah: **{label.capitalize()}** ({confidence*100:.2f}%)")
            st.markdown("### ♻️ Cara Daur Ulang")
            st.markdown(info['recycling_info'])
            st.markdown("### 🌍 Dampak Lingkungan")
            st.markdown(info['impact'])
            st.markdown("### 🔥 Jejak Karbon")
            st.markdown(info['carbon_footprint'])


# Tab 2: Kategori Sampah
with tab2:
    st.subheader("📦 Kategori Sampah & Informasi Daur Ulang")
    for cat in CATEGORIES:
        col1, col2 = st.columns([1, 4])
        with col1:
            st.image(f"assets/icons/{cat}.png", use_container_width=True)
        with col2:
            info = recycle_guide[cat]
            st.markdown(f"## {cat.capitalize()}")
            st.markdown(f"**Bisa didaur ulang:** {'✅' if info['can_recycle'] else '❌'}")

            with st.expander("♻️ Cara Daur Ulang"):
                st.markdown(info['recycling_info'])

            with st.expander("🌍 Dampak Lingkungan"):
                st.markdown(info['impact'])

            with st.expander("🔥 Jejak Karbon"):
                st.markdown(info['carbon_footprint'])
        st.divider()

# Tab 3: Panduan Upload
with tab3:
    col1, spacer,col2 = st.columns([1, 0.1, 2])
    with col1:
        st.image("assets/sample_image.png", caption="Contoh Gambar yang Baik", use_container_width=True)
    with col2:
        st.subheader("📷 Panduan Upload Gambar")
        st.markdown("""
        Agar hasil prediksi lebih akurat:
        - Gambar terang dan tidak blur 
        - Fokus hanya pada satu jenis sampah
        - Hindari latar belakang ramai
        - Pastikan benda sampah tidak terpotong
        """)  

# Tab 4: Tentang Kami
with tab4:
    col1, spacer,col2 = st.columns([1, 0.1, 2])
    with col1:
        st.image("assets/sampah.jpg", caption="Ilustrasi tumpukan sampah di Indonesia", use_container_width=True)
    with col2:
        st.image("assets/logo_recyclelens.png", width=400)
        st.write("""
        Indonesia menghadapi tantangan besar dalam pengelolaan sampah. Menurut data [SIPSN 2024](https://sipsn.menlhk.go.id), hanya sekitar 60% dari total 33,6 juta ton sampah yang berhasil dikelola dengan baik setiap tahun. Selebihnya berpotensi mencemari lingkungan dan menyebabkan kerusakan jangka panjang.

        **RecycleLens** dikembangkan sebagai solusi berbasis kecerdasan buatan untuk:
        - Mengklasifikasikan sampah dari gambar
        - Memberikan edukasi dan saran daur ulang
        - Mendorong masyarakat untuk lebih sadar lingkungan

        Proyek ini merupakan bagian dari **Capstone Laskar AI 2025 (LAI25-SM014)** yang beranggotakan:
        - A184YBM526 – Agum Medisa – Universitas Andalas 
        - A873XAF389 – Oryza Khairunnisa – Tokyo Metropolitan University 
        - A012XBF173 – Filza Rahma Muflihah – Universitas Telkom 
        - A010YBM333 – Muhammad Nafriel Ramadhan – Universitas Indonesia 
        """)



