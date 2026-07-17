import streamlit as st
import pandas as pd

# Load data
df = pd.read_excel("Jadwal_Guru.xlsx")

st.title("Sistem Informasi Jadwal Guru")

# Dropdown Nama Guru
# Ubah bagian ini di baris 10 dan 14
mapel_pilihan = st.selectbox("Pilih Mapel:", df['Mapel'].unique())

# Filter data berdasarkan Mapel yang dipilih
jadwal_guru = df[df['Mapel'] == mapel_pilihan]
# Menampilkan jadwal Senin-Sabtu
hari = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
for h in hari:
    st.subheader(h)
    data_hari = jadwal_guru[jadwal_guru['Hari'] == h]
    if not data_hari.empty:
        st.table(data_hari[['Jam', 'Mapel', 'Kelas']])
    else:
        st.write("Tidak ada jadwal.")
