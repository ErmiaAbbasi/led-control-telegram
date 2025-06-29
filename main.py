import serial
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

arduino = serial.Serial('SERIAL_PORT', 9600) #SERIAL_PORT example = COM12

BOT_TOKEN = 'YOUR_BOT_TOKEN' #insert your bot token here

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Send /on or /off")

async def turn_on(update: Update, context: ContextTypes.DEFAULT_TYPE):
    arduino.write(b'1')
    await update.message.reply_text("Turning ON")

async def turn_off(update: Update, context: ContextTypes.DEFAULT_TYPE):
    arduino.write(b'0')
    await update.message.reply_text("Turning OFF")

app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("on", turn_on))
app.add_handler(CommandHandler("off", turn_off))

app.run_polling()
