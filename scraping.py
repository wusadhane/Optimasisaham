from bs4 import BeautifulSoup
import pandas as pd
import requests
import streamlit as st

# mendapatkan data dari web tradingview
def getAllContent(date):
    url = (
        "https://id.tradingview.com/markets/stocks-indonesia/sectorandindustry-sector/"+date
    )
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    return [
        target["href"].split("/")[4].replace("-", " ")
        for target in soup.select(".tv-screener__symbol")
    ]

def spesificContent(target):
    url = (
        "https://id.tradingview.com/markets/stocks-indonesia/sectorandindustry-sector/"
        + target.replace(" ", "-")
    )
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    return [target.text for target in soup.select(".tv-screener__symbol")]

def getSektor():
    url = (
        "https://id.tradingview.com/markets/stocks-indonesia/sectorandindustry-sector/"
    )
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    return [
        target["href"].split("/")[4].replace("-", " ")
        for target in soup.select(".tv-screener__symbol")
    ]


def getSubSektor(sektor):
    url = (
        "https://id.tradingview.com/markets/stocks-indonesia/sectorandindustry-sector/"
        + sektor.replace(" ", "-")
        + "/industries/"
    )
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    return [
        target["href"].split("/")[4].replace("-", " ")
        for target in soup.select(".tv-screener__symbol")
    ]

def getEmiten(subsektor):
    url = (
        "https://id.tradingview.com/markets/stocks-indonesia/sectorandindustry-industry/"
        + subsektor.replace(" ", "-")
    )
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    return [target.text for target in soup.select(".tv-screener__symbol")]
