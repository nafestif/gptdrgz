import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.getenv("7733072125:AAHiDpo1tDCnsdSA4xQ2tpEz1VO-cE8ZXvM")
ADMIN_USERNAME = os.getenv("@rrrrrkkkskksk")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Привет, {update.effective_user.first_name}! Я бот 🤖")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

if __name__ == '__main__':
    print("Бот запущен...")
    app.run_polling()
