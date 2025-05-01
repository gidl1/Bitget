import streamlit as st
import json
import os
from datetime import datetime, timedelta
import pandas as pd
import random
import plotly.graph_objects as go

# Seiteneinstellungen
st.set_page_config(page_title="📊 Trading-Bot Dashboard", layout="wide")

# Stil (helles Layout)
st.markdown(
    """
    <style>
    .main { background-color: #f9fafb; }
    .block-container { padding-top: 2rem; }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("📈 Trading-Bot Dashboard")

# ──────────────────────────────────────────────
# Seitenleiste: Konfiguration & Optionen
# ──────────────────────────────────────────────
with st.sidebar:
    st.header("⚙️ Einstellungen")

    if os.path.exists("config.json"):
        with open("config.json") as f:
            config = json.load(f)
        st.json(config)
    else:
        st.warning("Keine config.json gefunden.")

    st.markdown("---")
    if st.button("🔁 Bot neustarten (Platzhalter)"):
        st.info("🔄 Neustart ausgelöst (funktioniert nur serverseitig)")

# ──────────────────────────────────────────────
# Obere Kennzahlen / Metriken
# ──────────────────────────────────────────────
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("🪙 Aktives Handelspaar", "BTC/USDT")
with col2:
    st.metric("📉 Letzter RSI", "29.7")
with col3:
    st.metric("📦 Offene Positionen", "1")

# ──────────────────────────────────────────────
# RSI-Chart (Beispieldaten, ersetzbar mit Live-RSI)
# ──────────────────────────────────────────────
st.subheader("📉 RSI-Verlauf")

rsi_data = {
    "Zeit": pd.date_range(end=datetime.now(), periods=30, freq="2min"),
    "RSI": [random.randint(20, 80) for _ in range(30)]
}
df_rsi = pd.DataFrame(rsi_data)

fig_rsi = go.Figure()
fig_rsi.add_trace(go.Scatter(x=df_rsi["Zeit"], y=df_rsi["RSI"],
                             mode='lines+markers', name="RSI", line=dict(color='royalblue')))
fig_rsi.update_layout(
    title="RSI über Zeit",
    xaxis_title="Zeit",
    yaxis_title="RSI",
    yaxis=dict(range=[0, 100]),
    height=400,
    template="plotly_white"
)
st.plotly_chart(fig_rsi, use_container_width=True)

# ──────────────────────────────────────────────
# Kapitalentwicklung / Kontoentwicklung (Beispiel)
# ──────────────────────────────────────────────
st.subheader("📈 Kapitalentwicklung")

kapital_data = {
    "Zeit": pd.date_range(end=datetime.now(), periods=20, freq="10min"),
    "Kapital ($)": [1000 + random.uniform(-30, 50) * i for i in range(20)]
}
df_kapital = pd.DataFrame(kapital_data)

fig_kap = go.Figure()
fig_kap.add_trace(go.Scatter(x=df_kapital["Zeit"], y=df_kapital["Kapital ($)"],
                             mode='lines+markers', line=dict(color='green')))
fig_kap.update_layout(
    title="Kapitalentwicklung",
    xaxis_title="Zeit",
    yaxis_title="USD",
    height=400,
    template="plotly_white"
)
st.plotly_chart(fig_kap, use_container_width=True)

# ──────────────────────────────────────────────
# Letzte Trades (simuliert / Live-Daten möglich)
# ──────────────────────────────────────────────
st.subheader("🧾 Letzte Trades")

trade_data = [
    {"Zeit": "14:01", "Symbol": "BTC/USDT", "Aktion": "Kauf", "Preis": 42780},
    {"Zeit": "13:30", "Symbol": "ETH/USDT", "Aktion": "Verkauf", "Preis": 2240}
]
st.table(trade_data)

# ──────────────────────────────────────────────
# Statusanzeige
# ──────────────────────────────────────────────
st.caption(f"Zuletzt aktualisiert: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

