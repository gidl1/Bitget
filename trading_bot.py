import os
import time
import random
import json
from datetime import datetime
from rsi_utils import calculate_rsi
from telegram_utils import send_telegram_message

def run_bot():
    # Beispiel-Konfiguration (ersetzt mit echten API-Keys und Parametern)
    config = {
        "symbols": ["BTC/USDT", "ETH/USDT"],
        "rsi_buy_threshold": 30,
        "rsi_sell_threshold": 70,
        "investment_amount": 100,
        "test_mode": True
    }
    
    while True:
        for symbol in config["symbols"]:
            try:
                # Simuliere RSI-Werte (ersetze dies mit einer echten API-Abfrage)
                rsi = random.randint(20, 80)
                print(f"[{symbol}] RSI: {rsi}")
                
                if rsi < config["rsi_buy_threshold"]:
                    print(f"[{symbol}] Kauf-Signal!")
                    # Hier würde der Kauf durchgeführt
                    send_telegram_message(f"Kauf-Befehl: {symbol} RSI: {rsi}")
                
                elif rsi > config["rsi_sell_threshold"]:
                    print(f"[{symbol}] Verkauf-Signal!")
                    # Hier würde der Verkauf durchgeführt
                    send_telegram_message(f"Verkaufs-Befehl: {symbol} RSI: {rsi}")
            
            except Exception as e:
                err_msg = f"[{symbol}] Fehler: {str(e)}"
                print(err_msg)
                send_telegram_message(f"⚠️ Fehler: {err_msg}")
            
            time.sleep(60)  # Warten, bevor das nächste Handelspaar abgefragt wird

if __name__ == "__main__":
    run_bot()

