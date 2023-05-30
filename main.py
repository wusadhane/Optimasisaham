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


dropdown = st.selectbox(
    "Pilih Saham", key='pilih_saham')

if dropdown:
    start_predict = st.date_input(
        "Tanggal Awal Optimasi", value=pd.to_datetime("2023-01-01"), min_value=pd.to_datetime("2023-01-01"), key='input_start')

    end_predict = st.date_input("Tanggal Akhir Optimasi",
                                value=pd.to_datetime("today"), key='input_end')

periode = (start_predict - end_predict).days - 1


st.button(label="Proses", key="Proses",on_click=None)
