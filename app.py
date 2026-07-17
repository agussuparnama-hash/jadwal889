import streamlit as st
import pandas as pd

# Load data
df = pd.read_excel("Jadwal_Guru.xlsx")

st.title("Sistem Informasi Jadwal Guru")

# Dropdown Nama Guru
nama_guru = st.selectbox("Pilih Nama Guru:", df['Nama_Guru'].unique())

# Filter data berdasarkan guru
jadwal_guru = df[df['Nama_Guru'] == nama_guru]

# Menampilkan jadwal Senin-Sabtu
hari = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
for h in hari:
    st.subheader(h)
    data_hari = jadwal_guru[jadwal_guru['Hari'] == h]
    if not data_hari.empty:
        st.table(data_hari[['Jam', 'Mapel', 'Kelas']])
    else:
        st.write("Tidak ada jadwal.")