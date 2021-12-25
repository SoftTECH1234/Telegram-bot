import os
import telebot

bot = telebot.TeleBot("API Key Here")

@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(message,"Hello! I am Visual code BOT")

@bot.message_handler(commands=["how"])
def send_message(message):
    bot.send_message(message, "https://www.telegram.com/@chathurahansaka")

  bot.polling()