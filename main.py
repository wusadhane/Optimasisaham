import streamlit as st
import numpy as np
import pandas as pd
import datetime
import yfinance as yf
from datetime import datetime
from dateutil.relativedelta import relativedelta

#datetime
start = datetime.now()
end = start - relativedelta(years=1)

#get data saham
saham = ['BBRM.JK','BESS.JK','BSML.JK','BULL.JK', 'CANI.JK', 'HAIS.JK','HITS.JK','IPCC.JK', 'MITI.JK', 'NELY.JK', "PSSI.JK", "RIGS.JK", "SHIP.JK", "SMDR.JK", "SOCI.JK", "TCPI.JK", "TMAS.JK", "TPMA.JK", "WINS.JK" ]
get_saham = yf.download(saham, start=end, end=start)
harga = get_saham["Close"].dropna(how="all")

st.title("Optimasi Portofolio Saham")
st.markdown(
    "Index Harga Saham Gabungan Sektor Transportasi Laut")

st.number_input("Masukan Dana Anda", key="dana")

d = st.date_input(
    "Tanggal Awal Optimasi",
    datetime.date(2022, 1, 1), key="start")


namasaham = st.selectbox(
    'Pilih saham',
    ('BBRM.JK','BESS.JK','BSML.JK','BULL.JK', 'CANI.JK', 'HAIS.JK','HITS.JK','IPCC.JK', 'MITI.JK', 'NELY.JK', "PSSI.JK", "RIGS.JK", "SHIP.JK", "SMDR.JK", "SOCI.JK", "TCPI.JK", "TMAS.JK", "TPMA.JK", "WINS.JK"))



st.button(label="Proses", key="Proses",on_click=None)
