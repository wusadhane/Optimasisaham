from bs4 import BeautifulSoup
import pandas as pd
import requests
import streamlit as st

# membuat dataframe harga saham
df = pd.Dataframe()

nama_saham = []
harga_saham = []



# mendapatkan data dari web trading view bs4
def getAllContent():
    url = (
        "https://id.tradingview.com/markets/stocks-indonesia/sectorandindustry-sector/"
    )
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    return [
        target["href"].split("/")[4].replace("-", " ")
        for target in soup.select(".tv-screener__symbol")
    ]
  
def spesificContent(target):
    url = (
        "https://www.tradingview.com/markets/stocks-indonesia/sectorandindustry-industry/marine-shipping/"
        + target.replace(" ", "-")
    )
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    return [target.text for target in soup.select(".tv-screener__symbol")]

