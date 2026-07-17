import streamlit as st
import pandas as pd

st.title("Sistem Informasi Jadwal Guru")

# Membaca data
@st.cache_data
def load_data():
    return pd.read_excel('Jadwal_Guru.xlsx')

df = load_data()

# Sidebar untuk filter
st.sidebar.header("Pilih Filter")

# Dropdown untuk Mapel
list_mapel = sorted(df['Mapel'].unique())
pilihan_mapel = st.sidebar.selectbox("Pilih Mata Pelajaran:", list_mapel)

# Dropdown untuk Kode berdasarkan Mapel yang dipilih
df_filter_mapel = df[df['Mapel'] == pilihan_mapel]
list_kode = sorted(df_filter_mapel['Kode_Mapel'].unique())
pilihan_kode = st.sidebar.selectbox("Pilih Kode:", list_kode)

# Filter Data Utama
hasil = df[(df['Mapel'] == pilihan_mapel) & (df['Kode_Mapel'] == pilihan_kode)]

# Menampilkan Jadwal berdasarkan hari
st.subheader(f"Jadwal untuk {pilihan_mapel} ({pilihan_kode})")

if not hasil.empty:
    # Mengurutkan berdasarkan hari (opsional: agar Senin-Sabtu berurutan)
    urutan_hari = ['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu']
    hasil['Hari'] = pd.Categorical(hasil['Hari'], categories=urutan_hari, ordered=True)
    hasil = hasil.sort_values('Hari')
    
    st.table(hasil[['Hari', 'Jam', 'Kelas']])
else:
    st.info("Tidak ada jadwal untuk kombinasi tersebut.")
