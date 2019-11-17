import telebot
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row('Hello', 'What`s app?')

TOKEN = "987787645:AAG-zq6lWQV84CFThd6eO1nL8nFjvNpXrhI"
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Hello, i`am TeleBot"
                                      "\n/help - помощь по командам")

@bot.message_handler(commands=["help"])
def start(message):
    bot.send_message(message.chat.id, "/start - начало работы с ботом\n/help - помощь в использовании")

@bot.message_handler(commands=["request"])
def start(message):
    bot.send_message(message.chat.id, "Введите соообщение которое будет отправлено на почту:")
@bot.message_handler(commands=["eblan"])
def start(message):
    bot.send_contact(message.chat.id, phone_number='+380 67 627 59 74')

@bot.message_handler(commands=["anime"])
def start(message):
    bot.send_message(message.chat.id, "https://yummyanime.club/")

if __name__ == '__main__':
    bot.polling()
