import streamlit as st
from pandas_datareader.data import DataReader
from pypfopt.discrete_allocation import DiscreteAllocation, get_latest_prices
from pypfopt import EfficientFrontier
from pypfopt import risk_models
from pypfopt import expected_returns
from pypfopt import plotting
import copy
import numpy as np
import pandas as pd
from pandas_datareader import data as pdr
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import yfinance as yf
import datetime
yf.pdr_override()

st.title("Optimasi Portofolio Saham")

st.markdown(
    "Index Harga Saham Gabungan Sektor Transportasi Laut")

start_date = "2023-01-01"
end_date = "2023-05-01"
tickers = ['BBRM.JK','BESS.JK','BSML.JK','BULL.JK', 'CANI.JK', 'HAIS.JK','HITS.JK','IPCC.JK', 'MITI.JK', 'NELY.JK', "PSSI.JK", "RIGS.JK", "SHIP.JK", "SMDR.JK", "SOCI.JK", "TCPI.JK", "TMAS.JK", "TPMA.JK", "WINS.JK" ]

thelen = len(tickers)
price_data = []
for ticker in range(thelen):
  prices = pdr.get_data_yahoo(tickers[ticker],start=start_date, end = end_date)
  price_data.append(prices.assign(ticker=ticker)[['Adj Close']])

#menampilkan data saham yang telah diambil
df_stocks = pd.concat(price_data, axis=1)
df_stocks.columns=tickers
df_stocks.head()

fig_price = px.line(df_stocks, title='Price of Individual Stocks')
fig_price.show()

daily_returns = df_stocks.pct_change().dropna()
daily_returns.head()

fig = px.line(daily_returns[['BBRM.JK','BESS.JK','BSML.JK','BULL.JK', 'CANI.JK', 'HAIS.JK','HITS.JK','IPCC.JK', 'MITI.JK', 'NELY.JK', "PSSI.JK", "RIGS.JK", "SHIP.JK", "SMDR.JK", "SOCI.JK", "TCPI.JK", "TMAS.JK", "TPMA.JK", "WINS.JK" ]], title='Daily Returns')
fig.show()

daily_returns.std()

sns.displot(data=daily_returns[['BBRM.JK','BESS.JK','BSML.JK','BULL.JK', 'CANI.JK', 'HAIS.JK','HITS.JK','IPCC.JK', 'MITI.JK', 'NELY.JK', "PSSI.JK", "RIGS.JK", "SHIP.JK", "SMDR.JK", "SOCI.JK", "TCPI.JK", "TMAS.JK", "TPMA.JK", "WINS.JK" ]], kind = 'kde', aspect = 2.5)
plt.xlim(-0.1, 0.1)

def plot_cum_returns(data, title):    
    daily_cum_returns = 1 + data.dropna().pct_change()
    daily_cum_returns = daily_cum_returns.cumprod()*100
    fig = px.line(daily_cum_returns, title=title)
    return fig
    
fig_cum_returns = plot_cum_returns(df_stocks, 'Cumulative Returns of Individual Stocks Starting with $100')
fig_cum_returns.show()

corr_df = df_stocks.corr().round(2) # round to 2 decimal places
fig_corr = px.imshow(corr_df, text_auto=True, title = 'Correlation between Stocks')
fig_corr.show()

mu = expected_returns.mean_historical_return(df_stocks)
S = risk_models.sample_cov(df_stocks)
print(mu)

def plot_efficient_frontier_and_max_sharpe(mu, S):  
    # Optimize portfolio for maximal Sharpe ratio 
    ef = EfficientFrontier(mu, S)
    fig, ax = plt.subplots(figsize=(8,6))
    ef_max_sharpe = copy.deepcopy(ef)
    plotting.plot_efficient_frontier(ef, ax=ax, show_assets=False)
    # Find the max sharpe portfolio
    ef_max_sharpe.max_sharpe(risk_free_rate=0.02)
    ret_tangent, std_tangent, _ =   ef_max_sharpe.portfolio_performance()
    ax.scatter(std_tangent, ret_tangent, marker="*", s=100, c="r",     label="Max Sharpe")
# Generate random portfolios
    n_samples = 1000
    w = np.random.dirichlet(np.ones(ef.n_assets), n_samples)
    rets = w.dot(ef.expected_returns)
    stds = np.sqrt(np.diag(w @ ef.cov_matrix @ w.T))
    sharpes = rets / stds
    ax.scatter(stds, rets, marker=".", c=sharpes, cmap="viridis_r")
# Output
    ax.set_title("Efficient Frontier with Random Portfolios")
    ax.legend()
    plt.tight_layout()
    plt.show()
    
plot_efficient_frontier_and_max_sharpe(mu, S)

ef = EfficientFrontier(mu, S)
ef.max_sharpe(risk_free_rate=0.02)
weights = ef.clean_weights()
print(weights)

weights_df = pd.DataFrame.from_dict(weights, orient = 'index')
weights_df.columns = ['weights']
weights_df

expected_annual_return, annual_volatility, sharpe_ratio = ef.portfolio_performance()
print('Expected annual return: {}%'.format((expected_annual_return*100).round(2)))
print('Annual volatility: {}%'.format((annual_volatility*100).round(2)))
print('Sharpe ratio: {}'.format(sharpe_ratio.round(2)))

df_stocks['Optimized Portfolio'] = 0
for ticker, weight in weights.items():
    df_stocks['Optimized Portfolio'] += df_stocks[ticker]*weight
df_stocks.head()

fig_cum_returns_optimized = plot_cum_returns(df_stocks['Optimized Portfolio'], 'Cumulative Returns of Optimized Portfolio Starting with $100')
fig_cum_returns_optimized.show()
