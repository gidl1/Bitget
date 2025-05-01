import requests
import os
from dotenv import load_dotenv

load_dotenv()

def send_telegram_message(message: str):
    """
    Sendet eine Nachricht an deinen Telegram-Chat.

    Nutzt TELEGRAM_BOT_TOKEN und TELEGRAM_CHAT_ID aus der .env-Datei.
    """
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")

    if not token or not chat_id:
        print("⚠️ Telegram-Token oder Chat-ID nicht gesetzt.")
        return

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message
    }

    try:
        response = requests.post(url, data=payload)
        if response.status_code != 200:
            print(f"❌ Telegram-Fehler: {response.text}")
    except Exception as e:
        print(f"❌ Telegram-Verbindungsfehler: {str(e)}")
