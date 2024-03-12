import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

# Load data
data_order_reviews = pd.read_csv("data_order_reviews_bersih.csv")
data_geolocation = pd.read_csv("data_geolocation_bersih.csv")
product_name = pd.read_csv("product_name_df.csv")

# Main content
st.title("Visualisasi Data Toko Online")

# Visualisasi Produk Terlaris
st.write("## Produk Terlaris")
max_products = product_name["product_category_name"].value_counts().head(5)
max_products_df = pd.DataFrame({
    'Nama Produk': max_products.index,
    'Total': max_products.values
})
st.write(max_products_df)

plt.figure(figsize=(10, 6))
top_product = max_products.idxmax()
max_products_sorted = max_products.sort_values()
max_products_sorted.plot(kind='barh', color=['skyblue' if prod != top_product else 'navy' for prod in max_products_sorted.index])
for i, val in enumerate(max_products_sorted.values):
    plt.text(val, i, f'{int(val)}', ha='left', va='center')
plt.title('Produk Terlaris')
plt.xlabel('Jumlah Pembelian')
plt.ylabel('Nama Produk')
plt.tight_layout()
plt_image_path = "produk_terlaris.png"
plt.savefig(plt_image_path)
st.image(plt_image_path, use_column_width=True)

# Visualisasi Produk Paling tidak Laris
st.write("## Produk Paling tidak Laris")
min_products = product_name["product_category_name"].value_counts().tail(5)
min_products_df = pd.DataFrame({
    'Nama Produk': min_products.index,
    'Total': min_products.values
})
st.write(min_products_df)

plt.figure(figsize=(10, 6))
top_product = min_products.idxmin()
min_products.plot(kind='barh', color=['navy' if prod == top_product else 'skyblue' for prod in min_products.index])
for i, val in enumerate(min_products.values):
    plt.text(val, i, f'{int(val)}', ha='left', va='center')
plt.title('Produk Paling tidak Laris')
plt.xlabel('Jumlah Pembelian')
plt.ylabel('Nama Produk')
plt.tight_layout()
plt_image_path = "produk_tidak_laris.png"
plt.savefig(plt_image_path)
st.image(plt_image_path, use_column_width=True)

# Visualisasi Histogram Skor Ulasan
st.write("## Histogram Skor Ulasan")
plt.figure(figsize=(10, 8))
plt.hist(data_order_reviews['review_score'], bins=5, color='skyblue', edgecolor='black')
plt.title('Histogram Skor Ulasan', fontsize=16, fontweight='bold')
plt.xlabel('Skor Ulasan', fontsize=12)
plt.ylabel('Jumlah Ulasan', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.tight_layout()
plt_image_path = "histogram_skor_ulasan.png"
plt.savefig(plt_image_path)
st.image(plt_image_path, use_column_width=True)

# Visualisasi Jumlah Pembeli per Kota
st.write("## Jumlah Pembeli per Kota")
jumlah_pembeli_per_state = data_geolocation['geolocation_state'].value_counts()
st.write(jumlah_pembeli_per_state)

plt.figure(figsize=(12, 8))
jumlah_pembeli_per_state.plot(kind='bar', color='skyblue')
plt.title('Jumlah Pembeli per Kota', fontsize=16, fontweight='bold')
plt.xlabel('Kota', fontsize=12)
plt.ylabel('Jumlah Pembeli', fontsize=12)
plt.xticks(rotation=45, ha='right', fontsize=10)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.tight_layout()
plt_image_path = "jumlah_pembeli_per_kota.png"
plt.savefig(plt_image_path)
st.image(plt_image_path, use_column_width=True)

# Visualisasi Top 10 Kota dengan Jumlah Pembeli Tertinggi
st.write("## Top 10 Kota dengan Jumlah Pembeli Tertinggi")
jumlah_pembeli_per_state = data_geolocation['geolocation_state'].value_counts()
top_10_states = jumlah_pembeli_per_state.head(10)
st.write(top_10_states)

plt.figure(figsize=(12, 8))
top_10_states.plot(kind='bar', color='skyblue')
plt.title('Top 10 Kota dengan Jumlah Pembeli Tertinggi', fontsize=16, fontweight='bold')
plt.xlabel('Kota', fontsize=12)
plt.ylabel('Jumlah Pembeli', fontsize=12)
plt.xticks(rotation=45, ha='right', fontsize=10)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.tight_layout()
plt_image_path = "top_10_kota_pembeli_tertinggi.png"
plt.savefig(plt_image_path)
st.image(plt_image_path, use_column_width=True)

# Visualisasi Proporsi Jumlah Pembeli per Kota (Top 10)
st.write("## Proporsi Jumlah Pembeli per Kota (Top 10)")
jumlah_pembeli_per_state = data_geolocation['geolocation_state'].value_counts()
top_10_states = jumlah_pembeli_per_state.head(10)
st.write(top_10_states)

plt.figure(figsize=(8, 8))
plt.pie(top_10_states, labels=top_10_states.index, autopct='%1.1f%%', colors=plt.cm.tab20.colors)
plt.title('Proporsi Jumlah Pembeli per Kota (Top 10)', fontsize=16, fontweight='bold')
plt.axis('equal')
plt.tight_layout()
plt_image_path = "proporsi_jumlah_pembeli_per_kota.png"
plt.savefig(plt_image_path)
st.image(plt_image_path, use_column_width=True)

with st.sidebar:
    # Menambahkan logo perusahaan
    st.image("logo_ecommerce.jpg")

# Kesimpulan
st.write("## Kesimpulan")
st.write("Berdasarkan data penjualan yang diberikan, dapat disimpulkan bahwa:")
st.write("1. Produk yang paling laris adalah 'cama_mesa_banho' dengan total penjualan sebanyak 3029 barang. Sementara itu, produk yang memiliki tingkat penjualan paling rendah adalah 'utilidades_domesticas' dengan total penjualan sebanyak 2335 barang.")
st.write("2. Tingkat kepuasan pelanggan terhadap layanan dan produk yang ditawarkan dapat dilihat dari data histogram skor ulasan. Lebih dari 5000 pelanggan memberikan rating tinggi, berkisar antara 4.5 hingga 5.")
st.write("3. Pada plot bar untuk jumlah pembeli per kota, dapat diamati bahwa Sao Paulo merupakan kota dengan tingkat pembelian tertinggi, mencapai jumlah sebesar 400.000 pembeli. Di sisi lain, kota Roraima menunjukkan tingkat pembelian terendah, hanya dengan 646 pembeli. Analisis ini menyoroti pola distribusi pembelian yang beragam di antara berbagai kota, dengan Sao Paulo menonjol sebagai pusat pembelian utama.")
