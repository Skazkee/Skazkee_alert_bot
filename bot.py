import os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Сначала получаем токен
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Проверяем, что токен существует
if not BOT_TOKEN:
    raise ValueError("Bot token is missing!")

# Выводим токен
print("BOT_TOKEN:", BOT_TOKEN)

MY_USER_ID = int(os.getenv("MY_USER_ID", "0"))

KEYWORDS = ["спам", "оплата", "взлом", "жалоба", "продам","Продам", "Продаю", "продаю", "Go-pro", "Go", "Го", "Гоу", "гоу"]

# Обработчик сообщений
def handle_message(update, context):
    message_text = update.message.text.lower()
    sender = update.message.from_user

    if any(word in message_text for word in KEYWORDS):
        alert = (
            f"🚨 Обнаружено ключевое слово!\n"
            f"👤 От: {sender.full_name} (@{sender.username})\n"
            f"🗨 Сообщение: {update.message.text}"
        )
        context.bot.send_message(chat_id=MY_USER_ID, text=alert)

def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # Обработчик текстовых сообщений
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    # Запуск бота
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
