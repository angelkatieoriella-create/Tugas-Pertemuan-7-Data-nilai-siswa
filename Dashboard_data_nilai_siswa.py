import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ========================
# KONFIGURASI HALAMAN
# ========================
st.set_page_config(
    page_title="Dashboard Analisis Siswa",
    layout="wide"
)

st.title("📊 Dashboard Analisis Hasil Siswa")

# ========================
# LOAD DATA
# ========================
@st.cache_data
def load_data():
    df = pd.read_excel("data_simulasi_50_siswa_20_soal.xlsx")
    return df

df = load_data()

# ========================
# TAMPILKAN DATA
# ========================
st.subheader("Data Siswa")
st.dataframe(df)

# ========================
# STATISTIK DASAR
# ========================
st.subheader("Statistik Nilai")

nilai_cols = df.select_dtypes(include='number')

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Rata-rata", round(nilai_cols.mean().mean(), 2))

with col2:
    st.metric("Nilai Tertinggi", nilai_cols.max().max())

with col3:
    st.metric("Nilai Terendah", nilai_cols.min().min())

# ========================
# VISUALISASI
# ========================
st.subheader("Distribusi Nilai")

fig, ax = plt.subplots()

nilai_cols.mean().plot(kind='bar', ax=ax)
ax.set_ylabel("Rata-rata Nilai")
ax.set_title("Rata-rata Nilai per Soal")

st.pyplot(fig)

# ========================
# FILTER DATA
# ========================
st.subheader("Filter Data")

kolom = st.selectbox("Pilih Soal", nilai_cols.columns)

minimum = st.slider(
    "Nilai Minimum",
    int(df[kolom].min()),
    int(df[kolom].max()),
    int(df[kolom].min())
)

filtered = df[df[kolom] >= minimum]

st.write(f"Jumlah siswa lolos filter: {len(filtered)}")
st.dataframe(filtered)