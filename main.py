import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import random

load_dotenv()

TOKEN = os.getenv("TELEGRAM_TOKEN")

if not TOKEN:
    raise ValueError("No se ha encontrado el token. Asegúrate de crear un archivo .env con TELEGRAM_TOKEN.")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hola Titan! Tratame con cariño')

# Función para el nuevo comando /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Comandos disponibles:\n/sort jugador1 jugador2 ... jugadorN - Arma dos equipos random con los jugadores pasados\n/help - Muestra este mensaje de ayuda")

async def sort_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Usaste mal el comando, fijate como se usa con /help")
        return

    jugadores = context.args
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

    salida_equipo1 = "Equipo claro: \n"
    num_jugador = 1
    for player in equipo1:
        salida_equipo1 = salida_equipo1 + str(num_jugador) + ". " + player + "\n"
        num_jugador += 1

    salida_equipo2 = "Equipo oscuro: \n"
    num_jugador = 1

    for player in equipo2:
        salida_equipo2 = salida_equipo2 + str(num_jugador) + ". " + player + "\n"
        num_jugador += 1

    await update.message.reply_text(salida_equipo1 + "\n" + salida_equipo2)

def main():
    application = Application.builder().token(TOKEN).build()

    # Handler para start
    application.add_handler(CommandHandler("start", start))

    # Handler para help
    application.add_handler(CommandHandler("help", help_command))
    
    # Handler para sort
    application.add_handler(CommandHandler("sort", sort_command))

    print("Bot iniciado...")
    application.run_polling()

if __name__ == '__main__':
    main()