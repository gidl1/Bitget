 🤖 Trading-Bot mit Streamlit Dashboard

Ein vollautomatischer Trading-Bot mit Web-Dashboard zur Überwachung in Echtzeit – lauffähig auf jedem VPS (z. B. Contabo).

## ✅ Funktionen

- Automatischer Handel basierend auf RSI
- Mehrere Handelspaare mit Wechselautomatik
- Stop-Loss & Take-Profit
- Telegram-Benachrichtigung
- 📊 Web-Dashboard mit Streamlit

## 🛠️ Installation

```bash
git clone https://github.com/dein-user/tradingbot.git
cd tradingbot
pip install -r requirements.txt
cp .env.example .env  # dann API-Schlüssel eintragen
```

## ▶️ Starten

Bot starten:
```bash
python trading_bot.py
```

Dashboard starten:
```bash
streamlit run dashboard.py
```

Dann im Browser öffnen: `http://localhost:8501` oder auf deinem Server.

## ⚙️ Konfiguration

Bearbeite `config.json` und `.env` nach deinen Bedürfnissen.

---

🚀 Bereit für den Live-Einsatz und jederzeit erweiterbar!
