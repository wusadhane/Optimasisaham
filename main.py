import streamlit as st
import numpy as np
import pandas as pd
import datetime


st.title("Optimasi Portofolio Saham")
st.markdown(
    "Index Harga Saham Gabungan Sektor Transportasi Laut")

st.number_input("Masukan Dana Anda", key="dana")

d = st.date_input(
    "Tanggal Awal Optimasi",
    datetime.date(2022, 1, 1), key="start")

st.button(label="Proses", key="Proses",on_click=None)
