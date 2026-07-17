import streamlit as st
import pandas as pd

st.title("Aplikasi Jadwal Guru")

# Pastikan nama file sesuai dengan yang Anda unggah
file_name = 'Jadwal_Guru.xlsx' 

try:
    # Membaca file excel
    data = pd.read_excel(file_name)
    
    # Menampilkan daftar kolom yang terdeteksi agar Anda bisa memastikannya
    st.write("### Daftar Kolom yang Ditemukan di File:")
    st.write(data.columns.tolist())
    
    # Membersihkan nama kolom (menghapus spasi di depan/belakang)
    data.columns = data.columns.str.strip()
    
    # Masukkan nama kolom yang Anda inginkan di sini
    # Sesuaikan dengan hasil daftar kolom di atas jika berbeda
    kolom_yang_dipakai = ['Jam', 'Mapel', 'Kelas']
    
    # Pengecekan apakah kolom tersebut ada
    if all(col in data.columns for col in kolom_yang_dipakai):
        st.subheader("Jadwal Guru")
        st.table(data[kolom_yang_dipakai])
    else:
        st.warning("Beberapa kolom yang dicari tidak ditemukan. Silakan sesuaikan nama kolom di kode dengan daftar kolom di atas.")
        st.table(data) # Menampilkan semua data agar Anda bisa melihat strukturnya

except FileNotFoundError:
    st.error(f"File '{file_name}' tidak ditemukan. Pastikan file tersebut sudah diunggah ke folder yang sama dengan app.py.")
except Exception as e:
    st.error(f"Terjadi kesalahan: {e}")
