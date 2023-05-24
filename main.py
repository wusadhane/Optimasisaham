import streamlit as st
import numpy as np
import pandas as pd
import datetime

st.title("Optimasi Portofolio Saham")
st.markdown(
    "Index Harga Saham Gabungan Sektor Transportasi Laut")

st.number_input("Masukan Dana Anda", key="dana")

d = st.date_input(
    "When\'s your birthday",
    datetime.date(2022, 1, 1), key="start")
st.write('Tanggal Awal:', d)

d = st.date_input(
    "When\'s your birthday",
    datetime.date(2023, 1, 1), key="end")
st.write('Tanggal Akhir:', d)
