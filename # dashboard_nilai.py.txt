# dashboard_nilai.py
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# --- Load Data ---
file_path = "data_simulasi_50_siswa_20_soal.xlsx"
df = pd.read_excel(file_path)

st.title("Dashboard Nilai Siswa - Simulasi 50 Siswa 20 Soal")

# --- Sidebar Filter ---
st.sidebar.header("Filter Dashboard")
siswa_list = df['Nama Siswa'].unique()
selected_siswa = st.sidebar.multiselect("Pilih Siswa:", siswa_list, default=siswa_list)

# Filter data
df_filtered = df[df['Nama Siswa'].isin(selected_siswa)]

# --- Tabel Data ---
st.subheader("Tabel Nilai Siswa")
st.dataframe(df_filtered)

# --- Rata-rata per Siswa ---
st.subheader("Rata-rata Nilai per Siswa")
df_filtered['Rata-rata'] = df_filtered.iloc[:, 1:].mean(axis=1)
fig, ax = plt.subplots(figsize=(10,5))
sns.barplot(x='Nama Siswa', y='Rata-rata', data=df_filtered, ax=ax)
plt.xticks(rotation=90)
st.pyplot(fig)

# --- Rata-rata per Soal ---
st.subheader("Rata-rata Nilai per Soal")
df_soal = df_filtered.iloc[:, 1:]  # asumsi kolom 0 = Nama Siswa
rata_per_soal = df_soal.mean()
fig2, ax2 = plt.subplots(figsize=(10,5))
sns.lineplot(x=rata_per_soal.index, y=rata_per_soal.values, marker="o", ax=ax2)
ax2.set_ylabel("Rata-rata Nilai")
ax2.set_xlabel("Soal")
st.pyplot(fig2)

# --- Distribusi Nilai Kelas ---
st.subheader("Distribusi Nilai Kelas")
fig3, ax3 = plt.subplots(figsize=(10,5))
sns.histplot(df_filtered['Rata-rata'], bins=10, kde=True, ax=ax3)
ax3.set_xlabel("Rata-rata Nilai")
st.pyplot(fig3)