from asyncio.base_futures import _future_repr_info
from matplotlib.lines import lineStyles
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import mplfinance as mpf
import yfinance as yf
from prophet import Prophet

dados = yf.download("AAPL", start="2023-01-01", end="2023-12-31", progress=False)
dados = dados.reset_index()

dados_treino = dados[dados['Date'] < '2023-07-31']
dados_teste = dados[dados['Date'] >= '2023-07-31']

dados_prophet_treino = dados_treino[['Date', 'Close']].rename(columns={'Date': 'ds', 'Close': 'y'})

modelo = Prophet(weekly_seasonality=True,
                 yearly_seasonality=True,
                 daily_seasonality=False)

modelo.add_country_holidays(country_name='US')

modelo.fit(dados_prophet_treino)

futuro = modelo.make_future_dataframe(periods=150)
previsao = modelo.predict(futuro)

plt.figure(figsize=(15,10))
plt.plot(dados_treino['Date'], dados_treino['Close'], label='Dados de Treino', color='yellow')
plt.plot(dados_teste['Date'], dados_teste['Close'], label='Dados Reais (Teste)', color='blue')
plt.plot(previsao['ds'], previsao['yhat'], label='Previsão', color='orange', linestyle='-')

# Corrigindo a linha vertical
inicio_previsao = dados_treino['Date'].max()
plt.axvline(inicio_previsao, color='green', linestyle='--', label='Inicio da previsão')

plt.xlabel('Data')
plt.ylabel('Preço de Fechamento')
plt.title('Previsão de Preço de Fechamento vs Dados Reais')
plt.legend()
plt.show()