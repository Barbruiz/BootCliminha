import requests
import datetime
import pywhatkit
import time

# ==== CONFIGURAÇÕES ====
api_key = "41bc41bcad730fbefc30d0b46c5b7780"  # <-- Substitua pela sua chave da API do OpenWeatherMap
cidade = "São Paulo"
numero_barbara = "+5511981339452"  # Ex: +5511999999999

# ==== FUNÇÃO: Obter Clima ====
def obter_clima():
    url = f"http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_key}&lang=pt_br&units=metric"
    resposta = requests.get(url)
    if resposta.status_code == 200:
        dados = resposta.json()
        temp = dados["main"]["temp"]
        descricao = dados["weather"][0]["description"]
        return f"{cidade} ({datetime.datetime.now().strftime('%Hh%M')}): {round(temp)}°C com {descricao}"
    else:
        return None

# ==== FUNÇÃO: Horóscopo (Escorpião) ====
def obter_horoscopo_escorpiao():
    return (
        "Você está mais intuitiva do que nunca. "
        "Confie nos seus instintos e não tenha medo de tomar decisões. "
        "Um momento ótimo para focar em projetos pessoais."
    )

# ==== FUNÇÃO: Fase da Lua (simplificada manual) ====
def obter_fase_da_lua():
    fases = ["Lua Nova", "Lua Crescente", "Lua Cheia", "Lua Minguante"]
    dia = datetime.datetime.now().day
    return fases[dia % 4]

# ==== MONTAR MENSAGEM ====
clima = obter_clima()
horoscopo = obter_horoscopo_escorpiao()
lua = obter_fase_da_lua()

mensagem = f"""Bom dia, Barbie! 🌞

📍 {clima if clima else "Não foi possível obter o clima agora."}
🔮 Escorpião hoje:
{horoscopo}
🌕 Fase da lua: {lua}

Tenha um ótimo dia!"""

# ==== AGENDAR ENVIO AUTOMÁTICO ====
agora = datetime.datetime.now()
hora = 10
minuto = 0

if agora.hour >= 10:
    # Agenda para o próximo dia
    agendamento = agora + datetime.timedelta(days=1)
else:
    agendamento = agora

print(f"Mensagem será enviada em {hora:02d}:{minuto:02d}. Abra o WhatsApp Web.")

# Espera até a hora certa
tempo_envio = datetime.datetime.combine(agendamento.date(), datetime.time(hour=hora, minute=minuto))
espera = (tempo_envio - agora).total_seconds()

if espera > 60:
    print(f"Esperando {int(espera)} segundos...")
    time.sleep(espera - 60)

# Envia a mensagem
pywhatkit.sendwhatmsg(numero_barbara, mensagem, hora, minuto)
