import streamlit as st
import numpy as np
import pandas as pd
import datetime
from scraping import nama_saham


# judul website
st.title("Optimasi Portofolio Saham")
st.markdown(
    "Index Harga Saham Gabungan Sektor Transportasi Laut")

# input dana 
st.number_input("Masukan Dana Anda", key="dana")

# dropdown saham
option = st.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone'))

st.write('You selected:', option)

# grafik
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

st.line_chart(chart_data)

# Tabel
st.table(nama_saham)

# Button proses
st.button(label="Proses", key="Proses",on_click=None)
