import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ===============================
# KONFIGURASI
# ===============================
st.set_page_config(
    page_title="Dashboard Analisis Siswa",
    layout="wide"
)

st.title("📊 Dashboard Analisis Data Simulasi 50 Siswa")

# ===============================
# LOAD DATA
# ===============================
@st.cache_data
def load_data():
    df = pd.read_excel("data_simulasi_50_siswa_20_soal.xlsx")
    return df

df = load_data()

st.subheader("Data Siswa")
st.dataframe(df)

# ===============================
# AMBIL KOLOM SOAL
# ===============================
soal = df.select_dtypes(include="number")

# ===============================
# NILAI SISWA
# ===============================
df["Total"] = soal.sum(axis=1)
df["Rata-rata"] = soal.mean(axis=1)

KKM = 75
df["Status"] = np.where(df["Rata-rata"] >= KKM,
                        "Tuntas", "Belum Tuntas")

# ===============================
# METRIK UTAMA
# ===============================
st.subheader("Ringkasan Kelas")

c1, c2, c3 = st.columns(3)

c1.metric("Jumlah Siswa", len(df))
c2.metric("Rata-rata Kelas", round(df["Rata-rata"].mean(),2))
c3.metric(
    "Ketuntasan (%)",
    f"{(df['Status'].eq('Tuntas').mean()*100):.1f}%"
)

# ===============================
# DISTRIBUSI NILAI
# ===============================
st.subheader("Distribusi Nilai Siswa")

fig, ax = plt.subplots()
sns.histplot(df["Rata-rata"], kde=True, ax=ax)
st.pyplot(fig)

# ===============================
# RATA-RATA PER SOAL
# ===============================
st.subheader("Rata-rata Nilai per Soal")

mean_soal = soal.mean()

fig2, ax2 = plt.subplots()
mean_soal.plot(kind="bar", ax=ax2)
ax2.set_ylabel("Nilai")
st.pyplot(fig2)

# ===============================
# ANALISIS TINGKAT KESUKARAN
# ===============================
st.subheader("Analisis Tingkat Kesukaran Soal")

kesukaran = soal.mean()/100

def kategori(p):
    if p < 0.3:
        return "Sulit"
    elif p <= 0.7:
        return "Sedang"
    else:
        return "Mudah"

analisis_soal = pd.DataFrame({
    "Soal": soal.columns,
    "Indeks Kesukaran": kesukaran.values,
    "Kategori": kesukaran.apply(kategori)
})

st.dataframe(analisis_soal)

# ===============================
# STATUS KETUNTASAN
# ===============================
st.subheader("Ketuntasan Siswa")

status = df["Status"].value_counts()

fig3, ax3 = plt.subplots()
status.plot(kind="pie", autopct="%1.1f%%", ax=ax3)
ax3.set_ylabel("")
st.pyplot(fig3)

# ===============================
# FILTER INTERAKTIF
# ===============================
st.subheader("Filter Siswa")

nilai_min = st.slider(
    "Minimum Rata-rata",
    int(df["Rata-rata"].min()),
    int(df["Rata-rata"].max()),
    70
)

filtered = df[df["Rata-rata"] >= nilai_min]

st.write(f"Siswa lolos filter: {len(filtered)}")
st.dataframe(filtered)