# Bot de Apuestas para LaLiga (Telegram + FootyStats)

Este bot monitorea partidos de LaLiga en tiempo real y te avisa vía Telegram cuando hay alta probabilidad de gol o córneres.

## Variables de entorno (Railway)

- `API_KEY`: tu API Key de FootyStats.
- `TELEGRAM_TOKEN`: token de tu bot de Telegram.
- `CHAT_ID`: tu ID de chat de Telegram.
- `CHECK_INTERVAL`: intervalo en segundos (ej: 60 para cada minuto).

## Cómo desplegarlo en Railway

1. Ve a [https://railway.app](https://railway.app) y crea un nuevo proyecto.
2. Conecta tu cuenta de GitHub.
3. Importa este repositorio.
4. Configura las variables de entorno.
5. Railway lo ejecutará automáticamente 24/7.