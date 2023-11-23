import telebot
from telebot import types
from config import BOT_TOKEN


bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start_command(message: types.Message):
    bot.send_message(
        chat_id=message.chat.id,
        text=f"Добро пожаловать! {message.from_user.username}"
    )
    
@bot.message_handler(commands=['help'])
def help_command(message: types.Message):
    bot.send_message(
        chat_id=message.chat.id,
        text="/start - Запуск Бота\n/help - Помощь"
    )

@bot.message_handler()
def echo(message: types.Message):
    bot.send_message(
        chat_id=message.chat.id,
        text=message.text
    )


if __name__ == '__main__':
    print("Бот работает")
    bot.infinity_polling()
