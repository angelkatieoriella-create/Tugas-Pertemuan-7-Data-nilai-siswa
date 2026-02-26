# Koding_Survey.py
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Judul aplikasi
st.title("Dashboard Data Nilai Siswa")

# Upload file CSV atau Excel
uploaded_file = st.file_uploader("Upload file CSV atau Excel", type=["csv", "xlsx"])

if uploaded_file is not None:
    # Cek ekstensi file
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)
    
    st.subheader("Preview Data")
    st.dataframe(df)

    # Pilih kolom untuk plot
    numeric_columns = df.select_dtypes(include=np.number).columns.tolist()
    if numeric_columns:
        st.subheader("Visualisasi Data")
        column_to_plot = st.selectbox("Pilih kolom untuk plot", numeric_columns)
        
        # Plot histogram
        fig, ax = plt.subplots()
        ax.hist(df[column_to_plot], bins=10, color='skyblue', edgecolor='black')
        ax.set_title(f"Histogram: {column_to_plot}")
        ax.set_xlabel(column_to_plot)
        ax.set_ylabel("Frekuensi")
        st.pyplot(fig)
    else:
        st.warning("Tidak ada kolom numerik untuk diplot.")
else:
    st.info("Silakan upload file CSV atau Excel terlebih dahulu.")