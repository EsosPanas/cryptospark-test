import streamlit as st
import ccxt
from datetime import datetime

st.set_page_config(page_title="CryptoSpark Test", layout="wide")
st.title("🚀 CryptoSpark AI - Versión de Prueba")
st.caption("Si ves esto funcionando → ya podemos añadir todo lo demás")

# Binance
exchange = ccxt.binanceusdm({'enableRateLimit': True})

st.subheader("📊 Precios en Vivo (Binance Futures)")
cols = st.columns(4)
symbols = ["BTC", "ETH", "SOL", "BNB"]

for i, sym in enumerate(symbols):
    try:
        ticker = exchange.fetch_ticker(f"{sym}/USDT:USDT")
        price = ticker['last']
        change = ticker['percentage']
        with cols[i]:
            st.metric(
                label=f"{sym}/USDT",
                value=f"${price:,.0f}",
                delta=f"{change:+.2f}%"
            )
    except:
        with cols[i]:
            st.metric(f"{sym}/USDT", "Error al cargar", "")

st.success("✅ ¡App funcionando! Actualiza la página para refrescar precios.")
st.info("Ahora vamos a añadir las alertas, IA y todo lo demás paso a paso.")
