import os
import sys
print(f"Python version: {sys.version}")
print(f"Installing dependencies...")


from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

BOT_TOKEN = os.getenv("BOT_TOKEN")
MY_USER_ID = int(os.getenv("MY_USER_ID", "0"))

KEYWORDS = ["спам", "оплата", "взлом", "жалоба"]

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message and update.message.text:
        message_text = update.message.text.lower()
        sender = update.message.from_user

        if any(word in message_text for word in KEYWORDS):
            alert = (
                f"🚨 Обнаружено ключевое слово!\n"
                f"👤 От: {sender.full_name} (@{sender.username})\n"
                f"🗨 Сообщение: {update.message.text}"
            )
            await context.bot.send_message(chat_id=MY_USER_ID, text=alert)

if __name__ == '__main__':
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()
