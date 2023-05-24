import streamlit as st
import numpy as np
import pandas as pd

st.title("Optimasi Portofolio Saham")
st.markdown(
    "Index Harga Saham Gabungan Sektor Transportasi Laut")

st.number_input("Masukan Dana Anda", key="dana")

start = st.date_input(
    "When\'s your birthday",
    datetime.date(2022, 1, 1))
st.write('Tanggal mulai:', start)

end = st.date_input(
    "When\'s your birthday",
    datetime.now())
st.write('Tanggal akhir:', end)
