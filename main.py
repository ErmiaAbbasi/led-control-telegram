import serial
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters,ConversationHandler, ContextTypes

arduino = serial.Serial('SERIAL_PORT', 9600) #SERIAL_PORT example = COM12

BOT_TOKEN = 'BOT_TOKEN' #insert your bot token here

ASK_INTENSITY = 0
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Send the intensity on the scale of 0 to 100.")
    return ASK_INTENSITY
async def intensity(update: Update, context: ContextTypes.DEFAULT_TYPE):
    intensity = update.message.text
    if not intensity.isdigit() or not (0 <= int(intensity) <= 100):
        await update.message.reply_text("Please enter a number between 0 and 100.")
        return ASK_INTENSITY
    arduino.write(bytes([int(intensity)]))
    await update.message.reply_text(f"Changed the intensity to {intensity}.")
async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    arduino.write(bytes([int('0')]))
    await update.message.reply_text("Canceled.")
    return ConversationHandler.END

app = ApplicationBuilder().token(BOT_TOKEN).build()
conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            ASK_INTENSITY: [MessageHandler(filters.TEXT & ~filters.COMMAND, intensity)]
        },
        fallbacks=[CommandHandler("cancel", cancel)]
    )
app.add_handler(conv_handler)

app.run_polling()
