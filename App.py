import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ===============================
# CONFIG HALAMAN
# ===============================
st.set_page_config(
    page_title="Dashboard Analisis Siswa",
    layout="wide"
)

st.title("📊 Dashboard Analisis Hasil Belajar Siswa")

# ===============================
# LOAD DATA
# ===============================
@st.cache_data
def load_data():
    df = pd.read_excel("data_simulasi_50_siswa_20_soal.xlsx")
    return df

df = load_data()

# ===============================
# SIDEBAR
# ===============================
st.sidebar.header("Menu Analisis")

menu = st.sidebar.radio(
    "Pilih Tampilan",
    ["Data Siswa", "Statistik Nilai", "Analisis Soal", "Visualisasi"]
)

# ===============================
# HITUNG NILAI TOTAL
# ===============================
df["Total_Nilai"] = df.sum(axis=1)

# ===============================
# 1. DATA SISWA
# ===============================
if menu == "Data Siswa":

    st.subheader("Data Jawaban Siswa")
    st.dataframe(df)

    st.metric(
        "Jumlah Siswa",
        len(df)
    )

# ===============================
# 2. STATISTIK NILAI
# ===============================
elif menu == "Statistik Nilai":

    st.subheader("Statistik Nilai Siswa")

    col1, col2, col3 = st.columns(3)

    col1.metric("Rata-rata", round(df["Total_Nilai"].mean(),2))
    col2.metric("Nilai Maksimum", df["Total_Nilai"].max())
    col3.metric("Nilai Minimum", df["Total_Nilai"].min())

    st.write("Deskripsi Statistik")
    st.write(df["Total_Nilai"].describe())

# ===============================
# 3. ANALISIS SOAL
# ===============================
elif menu == "Analisis Soal":

    st.subheader("Rata-rata Setiap Soal")

    mean_soal = df.drop(columns="Total_Nilai").mean()

    st.dataframe(mean_soal)

    fig, ax = plt.subplots()
    mean_soal.plot(kind="bar", ax=ax)
    plt.xticks(rotation=90)
    plt.ylabel("Rata-rata Skor")
    st.pyplot(fig)

# ===============================
# 4. VISUALISASI
# ===============================
elif menu == "Visualisasi":

    st.subheader("Distribusi Nilai Siswa")

    fig, ax = plt.subplots()
    sns.histplot(df["Total_Nilai"], kde=True)
    st.pyplot(fig)

    st.subheader("Heatmap Jawaban Siswa")

    fig2, ax2 = plt.subplots(figsize=(10,6))
    sns.heatmap(df.drop(columns="Total_Nilai"), cmap="YlGnBu")
    st.pyplot(fig2)