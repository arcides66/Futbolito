import requests
import time
import os
from datetime import datetime
import pytz

# Variables de entorno (Railway las usará automáticamente)
API_KEY = os.getenv("API_KEY")
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
CHECK_INTERVAL = int(os.getenv("CHECK_INTERVAL", 60))

HEADERS = {
    "accept": "application/json",
    "Authorization": f"{API_KEY}"
}

def enviar_telegram(mensaje):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": mensaje
    }
    requests.post(url, data=data)

def obtener_partidos_laliga():
    url = "https://api.footystats.org/live-matches?country=Spain&league=LaLiga"
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        return response.json().get("data", [])
    return []

def analizar_y_notificar():
    partidos = obtener_partidos_laliga()
    for partido in partidos:
        equipo_local = partido['home']['name']
        equipo_visitante = partido['away']['name']
        minuto = partido.get("minute", 0)

        gol_local_1T = partido.get("home", {}).get("probabilityToScoreFirstHalf", 0)
        gol_visitante_1T = partido.get("away", {}).get("probabilityToScoreFirstHalf", 0)

        corners_local = partido.get("home", {}).get("cornerPrediction", 0)
        corners_visitante = partido.get("away", {}).get("cornerPrediction", 0)

        if gol_local_1T > 70:
            enviar_telegram(f"Minuto {minuto}: {equipo_local} tiene {gol_local_1T}% de anotar antes del 45'.")
        if gol_visitante_1T > 70:
            enviar_telegram(f"Minuto {minuto}: {equipo_visitante} tiene {gol_visitante_1T}% de anotar antes del 45'.")

        if minuto > 70:
            if corners_local > 70:
                enviar_telegram(f"Minuto {minuto}: {equipo_local} tiene {corners_local}% de probabilidad de realizar otro córner.")
            if corners_visitante > 70:
                enviar_telegram(f"Minuto {minuto}: {equipo_visitante} tiene {corners_visitante}% de probabilidad de realizar otro córner.")

if __name__ == "__main__":
    while True:
        print("Revisando partidos...")
        analizar_y_notificar()
        time.sleep(CHECK_INTERVAL)