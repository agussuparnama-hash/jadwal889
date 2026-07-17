import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO

# --- 1. Fungsi untuk konversi tabel ke gambar ---
def df_to_image(df):
    # 1. Menambah ukuran kanvas (figsize) agar lebih lega
    fig, ax = plt.subplots(figsize=(10, 5)) 
    ax.axis('off')
    
    # 2. Membuat tabel dengan lokasi center
    table = ax.table(cellText=df.values, colLabels=df.columns, loc='center', cellLoc='center')
    
    # 3. Mengatur font dan ukuran
    table.auto_set_font_size(False)
    table.set_fontsize(12)
    
    # 4. Memberi padding pada setiap sel (lebar dan tinggi)
    for (row, col), cell in table.get_celld().items():
        cell.set_height(0.15)  # Mengatur tinggi baris
        cell.set_width(0.18)   # Mengatur lebar kolom
        
    # 5. Memberi ruang di sekeliling tabel
    plt.tight_layout(pad=3.0) 
    
    # 6. Menggunakan bbox_inches='tight' agar tidak terpotong
    buf = BytesIO()
    plt.savefig(buf, format='jpg', dpi=300, bbox_inches='tight') 
    buf.seek(0)
    return buf

# --- 2. Load Data ---
@st.cache_data
def load_data():
    return pd.read_excel('Jadwal_Guru.xlsx')

df = load_data()
df.columns = df.columns.str.strip() # Membersihkan spasi pada nama kolom

st.title("Aplikasi Jadwal Guru")

# --- 3. Filter Sidebar ---
st.sidebar.header("Pilih Filter")
list_mapel = sorted(df['Mapel'].unique())
pilihan_mapel = st.sidebar.selectbox("Pilih Mata Pelajaran:", list_mapel)

df_filter_mapel = df[df['Mapel'] == pilihan_mapel]
list_kode = sorted(df_filter_mapel['Mapel'].unique())
pilihan_kode = st.sidebar.selectbox("Pilih Kode:", list_kode)

# --- 4. Logika Menampilkan Data ---
hasil = df[(df['Mapel'] == pilihan_mapel) & (df['Mapel'] == pilihan_kode)]

st.subheader(f"Jadwal untuk {pilihan_mapel} ({pilihan_kode})")

if not hasil.empty:
    # Mengurutkan berdasarkan hari
    urutan_hari = ['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu']
    hasil['Hari'] = pd.Categorical(hasil['Hari'], categories=urutan_hari, ordered=True)
    hasil = hasil.sort_values('Hari')
    
    # Menampilkan tabel di layar
    st.table(hasil[['Hari', 'Jam Ke', 'Waktu', 'Rombel']])
    
    # --- 5. Tombol Download JPG ---
    img_buffer = df_to_image(hasil[['Hari', 'Jam Ke', 'Waktu', 'Rombel']])
    st.download_button(
        label="Download Jadwal sebagai JPG",
        data=img_buffer,
        file_name="jadwal_guru.jpg",
        mime="image/jpeg"
    )
else:
    st.info("Tidak ada jadwal untuk kombinasi tersebut.")
