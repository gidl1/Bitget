import ccxt
import time
import json
import os
from dotenv import load_dotenv
from rsi_utils import calculate_rsi
from telegram_utils import send_telegram_message

# .env laden
load_dotenv()

# Konfiguration laden
with open("config.json", "r") as f:
    config = json.load(f)

# Börse konfigurieren
exchange = ccxt.bitget({
    'apiKey': os.getenv("API_KEY"),
    'secret': os.getenv("API_SECRET"),
    'enableRateLimit': True
})

# Parameter aus der config
symbols = config["symbols"]
investment = config["investment_amount"]
rsi_buy = config["rsi_buy_threshold"]
timeframe = config["timeframe"]
sleep_time = config["sleep_time"]
test_mode = config.get("test_mode", True)

def fetch_closing_prices(symbol, tf="5m", limit=100):
    """Holt Schlusskurse (Close) für RSI"""
    try:
        ohlcv = exchange.fetch_ohlcv(symbol, timeframe=tf, limit=limit)
        return [candle[4] for candle in ohlcv]  # Close-Preise
    except Exception as e:
        print(f"[{symbol}] Fehler beim Laden der Daten: {e}")
        return []

# Hauptloop
while True:
    for symbol in symbols:
        try:
            closes = fetch_closing_prices(symbol, timeframe)
            if not closes:
                continue

            rsi = calculate_rsi(closes)
            print(f"[{symbol}] RSI: {rsi}")

            if rsi is not None and rsi < rsi_buy:
                message = f"🟢 Kauf-Signal für {symbol} – RSI {rsi}"
                print(message)
                send_telegram_message(message)

                if not test_mode:
                    # Beispiel: Order ausführen
                    balance = exchange.fetch_balance()
                    usdt = balance['USDT']['free']
                    amount = investment / closes[-1]
                    exchange.create_market_buy_order(symbol, amount)
                    send_telegram_message(f"✅ Marktorder gesendet: {symbol}")
                else:
                    print("[TESTMODUS] → Keine echte Order gesendet.")
        except Exception as e:
            err_msg = f"[{symbol}] Fehler: {str(e)}"
            print(err_msg)
            send_telegram_message(f"⚠️ Fehler: {err_msg}")

    print(f"⏳ Warte {sleep_time} Sekunden...")
    time.sleep(sleep_time)
