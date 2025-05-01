import streamlit as st
import json
import os

st.set_page_config(page_title="Trading Bot Dashboard", layout="wide")
st.title("📊 Trading-Bot Dashboard")

# --- Sidebar: Konfiguration ---
st.sidebar.header("⚙️ Konfiguration laden")

config_path = "config.json"
if os.path.exists(config_path):
    with open(config_path, "r") as f:
        config = json.load(f)
        st.sidebar.success("✅ config.json gefunden")
        st.sidebar.write(config)
else:
    st.sidebar.error("❌ config.json nicht gefunden")

# --- Hauptbereich ---
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("📈 Aktives Handelspaar", config.get("symbols", ["-"])[0])

with col2:
    st.metric("📉 RSI Letzter Wert", "27.5")  # Dummywert, ggf. live einlesen

with col3:
    test_status = "Aktiviert" if config.get("test_mode", True) else "Deaktiviert"
    st.metric("🧪 Testmodus", test_status)

st.divider()

st.subheader("📋 Letzte (Beispiel-)Trades")
# Diese Liste später z. B. aus JSON/CSV lesen
trades = [
    {"Zeit": "14:12", "Symbol": "BTC/USDT", "Aktion": "Kauf", "Preis": 42700},
    {"Zeit": "13:55", "Symbol": "ETH/USDT", "Aktion": "Verkauf", "Preis": 2235},
]

st.table(trades)

st.info("📌 Hinweis: Diese Oberfläche zeigt aktuell nur statische Beispielwerte. Du kannst sie erweitern, um Live-Daten, Logdateien oder Datenbank-Infos anzuzeigen.")
