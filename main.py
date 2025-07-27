import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import random
import re

def extraer_lista(reply_text: str) -> list[str]:
    # Quita espacios en blanco al principio y al final y parte en líneas
    lineas = reply_text.strip().splitlines()

    # La primera línea se conserva tal cual
    resultado = [lineas[0].strip()]

    # Para las demás: elimina “n. ”, “n.”, “n)”, etc.
    patron = re.compile(r'^\s*\d+\s*[\.)-]?\s*')
    for linea in lineas[1:]:
        nombre = patron.sub('', linea).strip()
        if nombre:                      # evita líneas vacías
            resultado.append(nombre)

    return resultado

def sortear_jugadores(jugadores: list[str]) -> tuple[list[str], list[str]]:
    equipo1 = []
    equipo2 = []
    cantidad_jugadores = len(jugadores)
    index = cantidad_jugadores - 1
    while (index != (int(cantidad_jugadores / 2) - 1)):
        rand = random.randint(0, index)
        jugador = jugadores.pop(rand)
        equipo1.append(jugador)
        index -= 1

    equipo2 = jugadores
    return equipo1, equipo2

def formatear_equipo(equipo: list[str], nombre_equipo: str) -> str:
    salida = f"{nombre_equipo}:\n"
    for num_jugador, player in enumerate(equipo, start=1):
        salida += f"{num_jugador}. {player}\n"
    return salida

load_dotenv()

TOKEN = os.getenv("TELEGRAM_TOKEN")

if not TOKEN:
    raise ValueError("No se ha encontrado el token. Asegúrate de crear un archivo .env con TELEGRAM_TOKEN.")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hola Titan! Tratame con cariño')

# Función para el nuevo comando /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Comandos disponibles:\n"
        "/sort jugador1 jugador2 ... jugadorN - Arma dos equipos random con los jugadores pasados\n"
        "/sort_reply - Responde a un mensaje con una lista de jugadores y arma dos equipos random\n"
        "/help - Muestra este mensaje de ayuda")

async def sort_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Usaste mal el comando, fijate como se usa con /help")
        return

    jugadores = context.args

    equipo1, equipo2 = sortear_jugadores(jugadores)

    salida_equipo1 = formatear_equipo(equipo1, "Equipo claro")
    salida_equipo2 = formatear_equipo(equipo2, "Equipo oscuro")

    await update.message.reply_text(salida_equipo1 + "\n" + salida_equipo2)

async def sort_reply_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message

    replied = msg.reply_to_message

    if not replied or not replied.text:
        await msg.reply_text("Por favor, responde a un mensaje que contenga los nombres de los jugadores.")
        return

    textoParseado = extraer_lista(replied.text)

    titulo = textoParseado[0] 

    jugadores = textoParseado[1:]

    equipo1, equipo2 = sortear_jugadores(jugadores)

    salida_equipo1 = formatear_equipo(equipo1, "Equipo claro")
    salida_equipo2 = formatear_equipo(equipo2, "Equipo oscuro")

    mensaje = f"{titulo}\n\n{salida_equipo1}\n{salida_equipo2}"

    await update.message.reply_text(mensaje)

def main():
    application = Application.builder().token(TOKEN).build()

    # Handler para start
    application.add_handler(CommandHandler("start", start))

    # Handler para help
    application.add_handler(CommandHandler("help", help_command))
    
    # Handler para sort
    application.add_handler(CommandHandler("sort", sort_command))

    # Handler para sort_reply
    application.add_handler(CommandHandler("sort_reply", sort_reply_command))

    print("Bot iniciado...")
    application.run_polling()

if __name__ == '__main__':
    main()