import requests
import json

def send_telegram_message(message):
    bot_token = "DEIN_BOT_TOKEN"
    chat_id = "DEIN_CHAT_ID"
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message
    }
    response = requests.post(url, data=payload)
    return response.json()

