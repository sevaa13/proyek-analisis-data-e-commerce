import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

# Load data
data_order_reviews = pd.read_csv("main_data.csv")
data_geolokasi = pd.read_csv("main_data.csv")

# Visualisasi histogram skor ulasan
plt.figure(figsize=(8, 6))
plt.hist(data_order_reviews['review_score'], bins=5, color='skyblue', edgecolor='black')
plt.title('Histogram Skor Ulasan')
plt.xlabel('Skor Ulasan')
plt.ylabel('Jumlah Ulasan')

# Simpan plot sebagai objek
histogram_plot = plt

# Buat aplikasi Streamlit
st.title('Analisis Tingkat Kepuasan Pelanggan')
st.write('Pertanyaan 1: Bagaimana tingkat kepuasan pelanggan terhadap layanan dan produk yang ditawarkan?')

# Tampilkan histogram skor ulasan
st.subheader('Histogram Skor Ulasan')
st.pyplot(histogram_plot)

# Visualisasi jumlah pembeli per kota
plt.figure(figsize=(10, 6))
jumlah_pembeli_per_state = data_geolokasi['geolocation_state'].value_counts()
jumlah_pembeli_per_state.plot(kind='bar', color='skyblue')
plt.title('Jumlah Pembeli per Kota')
plt.xlabel('Kota')
plt.ylabel('Jumlah Pembeli')
plt.xticks(rotation=45)

# Simpan plot sebagai objek
bar_chart = plt

# Buat aplikasi Streamlit
st.title('Analisis Tingkat Pembelian')
st.write('Pertanyaan 2: Kota bagian mana yang memiliki tingkat pembelian tertinggi?')

# Tampilkan visualisasi jumlah pembeli per kota
st.subheader('Jumlah Pembeli per Kota')
st.pyplot(bar_chart)

# Kesimpulan untuk pertanyaan 1
st.write('Conclution pertanyaan 1: Bagaimana tingkat kepuasan pelanggan terhadap layanan dan produk yang ditawarkan? Tingkat kepuasan terhadap produk yang ditawarkan sangat tinggi. Histogram menunjukan bahwa 5000 pembeli memberikan rating 4.5-5')

# Kesimpulan untuk pertanyaan 2
st.write('Conclution pertanyaan 2: Pada plot bar di atas, Sao Paulo menjadi kota dengan tingkat pembelian tertinggi yaitu 400.000 pembeli, dan kota Roraima menjadi yang terendah yaitu 646 pembeli.')

with st.sidebar:
    # Menambahkan logo perusahaan
    image = st.image("logo_ecommerce.jpg")
